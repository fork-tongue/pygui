import collagraph as cg


def test_cgx_use_imported_component():
    from tests.data.container import Container

    container = {"type": "root"}
    gui = cg.Collagraph(event_loop_type=cg.EventLoopType.SYNC)
    gui.render(cg.h(Container), container)

    content = container["children"][0]
    # The container does not actually provide any dom element
    # so the first child should actually be the type that
    # is defined in the Content component.
    assert content["type"] == "content-example"


def test_cgx_use_imported_func_component():
    from tests.data.func_import import FuncImport

    container = {"type": "root"}
    gui = cg.Collagraph(event_loop_type=cg.EventLoopType.SYNC)
    gui.render(cg.h(FuncImport), container)

    content = container["children"][0]
    assert content["children"][1]["type"] == "example-func-component"
    assert content["children"][0]["type"] == "example-func-component"
