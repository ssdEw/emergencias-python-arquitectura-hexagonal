import pytest
from pytest import fixture

from contexts.shared.domain.bus.query import Query, QueryHandler
from contexts.shared.infrastructure.bus.query import (
    QueryNotRegisteredError,
    SimpleQueryBus,
)


class FakeQuery(Query):
    pass


class FakeQueryHandler(QueryHandler):
    def __call__(self, query: FakeQuery):
        raise RuntimeError("This works fine!")


class NotRegisteredQuery(Query):
    pass


@fixture
def simple_query_bus() -> SimpleQueryBus:
    bus = SimpleQueryBus()
    bus.register(FakeQuery, FakeQueryHandler())
    return bus


class TestSimpleQueryBus:
    @pytest.mark.asyncio
    async def test_should_return_a_response_successfully(self, simple_query_bus):
        with pytest.raises(RuntimeError, match="This works fine!"):
            await simple_query_bus.ask(FakeQuery())

    @pytest.mark.asyncio
    async def test_should_raise_an_exception_dispatching_a_non_registered_query(
        self, simple_query_bus
    ):
        with pytest.raises(QueryNotRegisteredError):
            await simple_query_bus.ask(NotRegisteredQuery())
