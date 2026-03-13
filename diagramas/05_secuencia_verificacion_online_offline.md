# Diagrama 05: Secuencia de Verificación Online/Offline

## Qué representa
Describe el proceso de validación de acceso en puerta bajo dos condiciones operativas: conectividad disponible y operación degradada sin red.

## Cómo funciona
1. El asistente presenta QR con ticket, versión, firma y expiración.
2. En modo online, el backend valida contra estado cacheado y estado on-chain.
3. En modo offline, el dispositivo aplica validación local y marca resultado provisional.
4. Al recuperar conectividad, se sincronizan consumos pendientes.
5. La resolución de conflictos aplica política: primer check-in sincronizado gana.

## Reglas operativas
- Ventana máxima offline: 30 minutos.
- Sincronización obligatoria de verificaciones provisionales.
- Eventos conflictivos pasan a revisión en bitácora operativa.

## Decisiones reflejadas
- Continuidad del acceso ante saturación o caída de red.
- Control de riesgo por reconciliación posterior.
- Autoridad de verificación compartida entre verificador y admin ticketera.

## Uso en la tesis
- Capítulo sugerido: diseño funcional y evaluación de riesgos.
- Propósito: justificar resiliencia operativa en eventos masivos.