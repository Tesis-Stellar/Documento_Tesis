# Diagrama 09: Mapa de Historias de Usuario

## Qué representa
Organiza el alcance funcional en épicas e historias para comunicar prioridades de implementación y criterios de aceptación en lenguaje de producto.

## Cómo funciona
1. Se agrupan historias por cuatro épicas: configuración B2B, reventa B2C, verificación y trazabilidad.
2. Cada historia conecta un rol con un objetivo verificable.
3. El mapa define el orden lógico de construcción del prototipo.

## Historias incluidas
- Épica 1: creación de evento, configuración de fees y despliegue por factory.
- Épica 2: listado de ticket, compra y ejecución atómica.
- Épica 3: validación online, validación offline y sincronización.
- Épica 4: historial por `root_id`, indexación on-chain y métricas académicas.

## Criterios de aceptación recomendados
- HU-06: la compra debe fallar completa si cualquier paso de pago o mint falla.
- HU-08: validación offline solo dentro de ventana de 30 minutos.
- HU-09: al sincronizar, conflictos se resuelven por primer check-in confirmado.
- HU-10: consultar trazabilidad de propietarios por ticket raíz y versiones.

## Uso en la tesis
- Capítulo sugerido: requerimientos y planeación de implementación.
- Propósito: enlazar objetivos académicos con entregables verificables.