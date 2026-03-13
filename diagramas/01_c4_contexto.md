# Diagrama 01: C4 Contexto del Sistema

## Qué representa
Este diagrama ubica la solución Stellar Tickets en su entorno organizacional y tecnológico, mostrando actores externos, límites del sistema y relaciones principales.

## Cómo funciona
1. La ticketera (cliente B2B) configura eventos y políticas desde el portal web.
2. Los usuarios finales comprador y vendedor interactúan con el marketplace de reventa.
3. La firma de transacciones se realiza en wallet no-custodial (Freighter).
4. El backend coordina lógica de negocio, indexa eventos on-chain y persiste datos off-chain.
5. El factory crea contratos por evento en Stellar Testnet.

## Actores y componentes clave
- Actores: comprador, vendedor, verificador, admin ticketera, admin plataforma.
- Componentes: frontend white-label, backend/indexador, PostgreSQL, factory, contrato de evento, testnet.

## Decisiones reflejadas
- Arquitectura B2B adaptable a distintas ticketeras.
- Contrato por evento para aislar configuración y fondos.
- Historial mixto: eventos mínimos on-chain y detalle en indexador off-chain.

## Uso en la tesis
- Capítulo sugerido: solución y arquitectura general.
- Propósito: definir alcance del sistema y límites de confianza.