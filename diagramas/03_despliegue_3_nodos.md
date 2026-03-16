# Diagrama 03: Despliegue en 3 Nodos

## Qué representa
Modela la topología mínima de ejecución para el prototipo académico: nodo web, nodo API y nodo de datos, con integración a Stellar Testnet.

## Cómo funciona
1. El nodo web expone portales para comprador, vendedor, verificador y administrador, accesibles desde navegador de escritorio o móvil.
2. El nodo API centraliza servicios de reventa, verificación, firma QR e indexación.
3. El nodo de datos persiste entidades de negocio y bitácora operativa.
4. Los servicios API interactúan con contratos en testnet y procesan eventos.
5. Las wallets de usuarios firman transacciones fuera del backend.

## Nodos y responsabilidades
- Nodo 1 Web: experiencia de usuario y administración.
- Nodo 2 API: lógica de dominio e integración blockchain.
- Nodo 3 Data: persistencia, auditoría y soporte analítico.

## Decisiones reflejadas
- Despliegue distribuido con separación funcional.
- Escalabilidad inicial por componentes desacoplados.
- Preparación para validación de métricas por capa.
- Posibilidad de acceso móvil sin app nativa, usando navegador y wallet compatible.

## Uso en la tesis
- Capítulo sugerido: implementación y despliegue.
- Propósito: demostrar viabilidad operativa en entorno académico.