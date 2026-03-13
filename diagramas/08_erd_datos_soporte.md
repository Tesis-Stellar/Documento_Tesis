# Diagrama 08: ERD de Datos de Soporte

## Qué representa
Especifica el modelo relacional off-chain para operar la solución y resolver consultas de negocio, auditoría y verificación de forma eficiente.

## Cómo funciona
1. Se registran usuarios, ticketeras y eventos con sus direcciones y parámetros.
2. Cada ticket lógico (`TICKET_ROOT`) mantiene sus versiones (`TICKET_VERSION`).
3. Las publicaciones de reventa y transacciones se vinculan a versiones específicas.
4. Los check-ins registran modo de verificación, dispositivo y sincronización.
5. La auditoría consolida eventos del negocio y referencias on-chain.

## Entidades clave
- `USUARIO`, `TICKETERA`, `EVENTO`.
- `TICKET_ROOT` y `TICKET_VERSION` para versionado por burn+remint.
- `LISTING_REVENTA`, `TRANSACCION_REVENTA`, `CHECKIN`, `AUDITORIA_EVENTO`.

## Decisiones reflejadas
- Historial mixto: mínimo en cadena, detalle y consulta fuera de cadena.
- Diseño preparado para trazabilidad por `root_id` y por `tx_hash`.
- Soporte para reconciliación de validaciones offline.

## Uso en la tesis
- Capítulo sugerido: diseño de datos e implementación backend.
- Propósito: justificar persistencia y consultas de alto volumen.