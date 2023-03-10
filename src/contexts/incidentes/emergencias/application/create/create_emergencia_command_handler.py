from contexts.incidentes.emergencias.application.create import (
    CreateEmergenciaCommand,
    EmergenciaCreator,
)
from contexts.incidentes.emergencias.domain.value_objects import (
    EmergenciaAbscisa,
    EmergenciaCode,
    EmergenciaId,
)
from contexts.incidentes.shared.domain.value_objects import UsuarioId
from contexts.shared.domain.bus.command import CommandHandler


class CreateEmergenciaCommandHandler(CommandHandler):
    def __init__(self, creator: EmergenciaCreator):
        self._creator = creator

    async def __call__(self, command: CreateEmergenciaCommand):  # type: ignore[override]
        _id = EmergenciaId(command.id)
        abscisa = EmergenciaAbscisa(command.abscisa)
        usuario_id = UsuarioId(command.usuario_id)

        await self._creator.create(_id=_id, abscisa=abscisa, usuario_id=usuario_id)
