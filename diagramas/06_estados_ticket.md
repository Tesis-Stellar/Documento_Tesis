# Diagrama 06: Máquina de Estados del Ticket

## Qué representa
Define el ciclo de vida del ticket desde su emisión inicial hasta su consumo final, incluyendo reventa múltiple, invalidación y versionamiento.

## Cómo funciona
1. El ticket nace en emisión primaria de tipo stub.
2. Se asigna a un comprador y puede entrar a estado de listado para reventa.
3. Si ocurre compra de reventa, se activa secuencia burn+remint.
4. La nueva versión vuelve al estado vigente y puede revenderse nuevamente.
5. El ticket termina como consumido al check-in exitoso o como invalidado por política del evento.

## Estados relevantes
- EmitidoStub, Asignado, Listado, Revendido, Verificado, Consumido, Invalidado.
- Subestado técnico Revendido: BurnPrevio → RemintNuevo → VersionVigente.

## Decisiones reflejadas
- Trazabilidad por `ticket_root_id` con versiones sucesivas.
- Invalidación explícita de versión anterior en cada reventa.
- Reventa múltiple permitida sin tope de precio en v1.

## Uso en la tesis
- Capítulo sugerido: modelo funcional del activo digital.
- Propósito: formalizar reglas de transición y condiciones terminales.