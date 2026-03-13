# Diagrama 04: Secuencia de Reventa Atómica

## Qué representa
Formaliza el flujo transaccional de reventa desde publicación hasta transferencia de propiedad, con política burn+remint y distribución de comisiones.

## Cómo funciona
1. El vendedor publica un ticket vigente en el marketplace.
2. El comprador inicia compra desde la interfaz web.
3. El backend invoca una operación atómica del contrato de evento.
4. En la misma transacción se ejecutan: transferencias de comisión, pago neto, burn de versión previa y mint de nueva versión.
5. El contrato emite evento on-chain para indexación y trazabilidad por `ticket_root_id`.

## Reglas de consistencia
- No hay estado intermedio aceptado entre pago y cambio de titularidad.
- La versión anterior queda inválida al finalizar la transacción.
- El nuevo titular recibe un comprobante asociado a la nueva versión.

## Decisiones reflejadas
- Contrato por evento desplegado desde factory.
- Política de reventa con precio libre y transparencia.
- Historial mixto: evento on-chain + consulta detallada en PostgreSQL.

## Uso en la tesis
- Capítulo sugerido: diseño del contrato inteligente.
- Propósito: demostrar prevención de inconsistencias y duplicidad lógica.