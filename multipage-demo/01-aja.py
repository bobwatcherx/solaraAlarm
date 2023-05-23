import solara

clicks = solara.reactive(0)


@solara.component
def Page():
    with solara.Column():
        solara.Button("tolol",color="red",style={"color":"white"})