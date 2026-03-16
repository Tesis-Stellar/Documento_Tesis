# Diagrama 10 - Modelo de Negocio y Flujo General

## Propósito

Mostrar de un solo vistazo cómo se conectan todos los actores, contratos y sistemas del proyecto Stellar Tickets: quién hace qué, en qué orden, y cómo fluye el dinero.

---

## Actores del sistema

| Actor | Qué hace | Herramienta que usa |
|---|---|---|
| **Administrador de plataforma** | Inicializa la factory una sola vez | Wallet Stellar (Freighter o CLI) |
| **Organizador del evento** | Crea el evento y los boletos | Wallet Stellar + portal admin |
| **Comprador** | Compra boletos y los revende | Wallet browser (Freighter) |
| **Verificador** | Escanea QR y redime boletos | App verificador (tableta) |

---

## Las dos capas del sistema

### Capa on-chain (blockchain Stellar)

Todo lo que es verdad absoluta y no se puede alterar:

- **`factory_contract`**: el contrato maestro de la plataforma. Valida que un evento sea legítimo y registra su contrato correspondiente.
- **`event_contract`**: una instancia por cada evento. Guarda el estado real de cada boleto. Un boleto existe aquí como propietario, precio y estado (disponible → vendido → redimido).

### Capa off-chain (servidores y base de datos)

Todo lo que facilita la experiencia de usuario y la velocidad:

- **Indexador**: lee los eventos que emite el contrato y los traduce a una base de datos rápida.
- **API REST**: sirve la información al portal web y a la app de verificación.
- **Portal Web**: donde el comprador conecta su wallet y firma transacciones.
- **App Verificador**: valida el QR del comprador comparando con el estado on-chain.

---

## Flujo paso a paso

```
1.  Admin inicializa factory (una única vez).
2.  Organizador configura el evento en factory.
3.  Factory registra el event_contract y emite EventoCreado.
4.  Organizador crea boletos con precio y capacidad.
5.  Event contract emite TicketMinted por cada boleto creado.
6.  Indexador escucha los eventos on-chain y los guarda en PostgreSQL.
7.  Base de datos queda actualizada.
8.  API sirve la lista de boletos disponibles al portal web.
9.  Comprador conecta su wallet en el portal.
10. Comprador firma la transacción de compra (comprar_boleto).
11. Contrato transfiere la propiedad y distribuye el pago on-chain.
12. Comprador recibe su QR de boleto (firmado on-chain).
13. En el evento, el verificador escanea el QR.
14. App verificador consulta el estado real en el contrato.
15. App llama redimir_boleto: el boleto queda marcado como usado para siempre.
```

---

## Flujo del dinero

El pago ocurre completamente on-chain en tokens Stellar:

```
Comprador paga → event_contract distribuye automáticamente:
  └── % organización  → wallet del organizador
  └── % plataforma    → wallet de la plataforma
```

No hay intermediario que retenga fondos. El contrato liquida en el mismo momento de la compra.

---

## Qué significa "cerrar el deploy" (pendiente técnico actual)

### Estado actual

`factory_contract` actúa como **registro**: el organizador o admin despliega manualmente un `event_contract` con la CLI de Soroban y luego registra esa dirección en el factory. Es un paso manual.

### Estado objetivo (cerrar el deploy)

`factory_contract` actúa como **verdadera factory**: al llamar `crear_evento_contrato(config)`, el propio contrato despliega una nueva instancia de `event_contract` internamente usando el mecanismo `deployer()` de Soroban.

```
Estado actual:
  1. Admin despliega event_contract manualmente → obtiene dirección
  2. Admin llama factory.crear_evento_contrato(config, direccion_manual)
  3. Factory registra la dirección

Estado objetivo (factory real):
  1. Admin llama factory.crear_evento_contrato(config)
  2. Factory despliega internamente el event_contract usando el WASM
  3. Factory inicializa el nuevo contrato con la config
  4. Factory devuelve la dirección del nuevo contrato
```

### Por qué importa

- Elimina el paso manual y el riesgo de registrar un contrato equivocado.
- Garantiza que todos los event_contracts de una plataforma vienen del mismo WASM validado.
- Es el patrón correcto para producción: "nadie puede registrar un contrato falso".
- Es también el patrón esperado en la documentación de Soroban para arquitecturas multi-contrato.

### Qué falta técnicamente para cerrarlo

1. Subir el WASM de `event_contract` a la red y obtener su hash.
2. Guardar ese hash en `factory_contract` (storage).
3. Reemplazar el parámetro `direccion_contrato_evento: Address` por el deploy interno:
   ```rust
   let contrato_nuevo = entorno
       .deployer()
       .with_address(entorno.current_contract_address(), salt)
       .deploy_v2(wasm_hash, (configuracion.clone(),));
   ```
4. Inicializar el contrato nuevo desde la factory antes de retornar.
5. Actualizar los tests para usar el nuevo flujo.
6. Desplegar factory en testnet y verificar el flujo completo.

---

## Para el lector no técnico

Imagina que la plataforma es una inmobiliaria:

- La **factory** es la oficina central que valida si un evento puede vender boletos.
- Cada **event_contract** es el contrato notarial de un evento específico (el concierto X, la obra Y).
- El **boleto** es como una escritura digital: tiene dueño registrado, precio pagado y fecha de transferencia, todo en cadena de bloques.
- El **indexador** es el archivo de búsqueda rápida: copia los datos de la cadena a una base de datos para que la web cargue rápido.
- La **web** es la inmobiliaria en línea donde el comprador ve y adquiere.
- El **verificador** es el notario en la puerta: confirma que el papel es auténtico y lo marca como "usado".

---

## Uso en la tesis

- **`solucion.tex`**: sección de arquitectura del sistema o flujo de negocio.
- **`marco_teorico.tex`**: comparación con sistemas tradicionales de ticketera.
- **`evaluacion y resultados.tex`**: validación del flujo completo E2E.
