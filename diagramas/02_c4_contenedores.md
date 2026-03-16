# Diagrama 02: C4 Contenedores

## Qué representa
Describe la descomposición técnica en contenedores de software y su integración entre cliente, backend, almacenamiento y blockchain.

## Cómo funciona
1. El frontend consume API para operaciones de listado, compra y verificación desde navegador desktop o móvil.
2. El backend separa módulos de autenticación, reventa, verificación e indexación.
3. PostgreSQL conserva identidad, operaciones y auditoría para consultas rápidas.
4. El contrato factory despliega contratos por evento en Stellar.
5. Los contratos procesan pagos en XLM y opcionalmente en USDC_SIM.

## Componentes clave
- Cliente: web ticketera, navegador móvil, Freighter y app o portal verificador.
- Servidor: API, auth, reventa, verificación QR, indexador, cola de sincronización.
- Datos: PostgreSQL, bitácora de auditoría, caché de estado de tickets.
- Blockchain: factory, contrato de evento, SAC XLM y token opcional.

## Decisiones reflejadas
- Custodia no-custodial para usuario final.
- Separación entre escritura on-chain y lectura optimizada off-chain.
- Soporte de continuidad operativa por cola de sincronización offline.

## Uso en la tesis
- Capítulo sugerido: sistema de arquitectura.
- Propósito: justificar distribución de responsabilidades técnicas.
- Lectura recomendada junto con `main_contract/README.md` para entender la estructura consolidada del monorepo.