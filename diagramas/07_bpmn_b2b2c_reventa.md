# Diagrama 07: BPMN del Proceso B2B2C de Reventa

## Qué representa
Modela el proceso extremo a extremo con enfoque organizacional, desde la configuración del evento por la ticketera hasta el acceso del usuario final.

## Cómo funciona
1. La ticketera crea evento y define wallets de comisión.
2. La plataforma despliega contrato por evento con factory y publica el marketplace.
3. El usuario conecta wallet, lista ticket y ejecuta compra.
4. El sistema entrega ticket vigente y habilita verificación de acceso.
5. El flujo de acceso contempla validación online o offline con reconciliación posterior.

## Lanes del proceso
- Ticketera B2B.
- Plataforma Stellar Tickets.
- Usuario final B2C.
- Verificación operativa en puerta.

## Decisiones reflejadas
- Separación de responsabilidades por actor.
- Integración entre gobierno de evento y operación de acceso.
- Inclusión explícita de continuidad operativa offline.

## Uso en la tesis
- Capítulo sugerido: procesos de negocio y operación.
- Propósito: mostrar coherencia entre arquitectura técnica y flujo operacional.