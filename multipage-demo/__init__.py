import solara
@solara.component
def Layout(children=[]):
    print("I get called before the Page component gets rendered")
    return solara.AppLayout(children=children)