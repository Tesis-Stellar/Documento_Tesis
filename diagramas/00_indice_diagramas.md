# Índice Maestro de Diagramas - Stellar Tickets

Este índice organiza el paquete de diagramas de alto nivel para su incorporación en la memoria de tesis.

## Estructura de entrega
Cada diagrama tiene dos archivos:
1. Archivo visual en Mermaid (`.mmd`).
2. Archivo explicativo (`.md`) con propósito, funcionamiento y uso académico.

## Catálogo
1. `01_c4_contexto.mmd` + `01_c4_contexto.md`
2. `02_c4_contenedores.mmd` + `02_c4_contenedores.md`
3. `03_despliegue_3_nodos.mmd` + `03_despliegue_3_nodos.md`
4. `04_secuencia_reventa_atomica.mmd` + `04_secuencia_reventa_atomica.md`
5. `05_secuencia_verificacion_online_offline.mmd` + `05_secuencia_verificacion_online_offline.md`
6. `06_estados_ticket.mmd` + `06_estados_ticket.md`
7. `07_bpmn_b2b2c_reventa.mmd` + `07_bpmn_b2b2c_reventa.md`
8. `08_erd_datos_soporte.mmd` + `08_erd_datos_soporte.md`
9. `09_historias_usuario_mapa.mmd` + `09_historias_usuario_mapa.md`
10. `10_modelo_negocio_flujo.mmd` + `10_modelo_negocio_flujo.md`

## Mapeo sugerido a capítulos de tesis
- `marco_teorico.tex`: 01, 02, 10.
- `solucion.tex`: 01, 02, 04, 06, 10.
- `sistema de arquitectura.tex`: 03, 05, 08.
- `requerimientos.tex` o sección equivalente: 09.
- `evaluacion y resultados.tex`: 05 y métricas derivadas de 04/08.

## Convenciones usadas
- Idioma: español.
- Nivel: alto nivel para alineación de diseño previo a implementación.
- Supuestos fijos: factory por evento, no-custodial, burn+remint, historial mixto on-chain/off-chain, validación online y offline con sincronización obligatoria.