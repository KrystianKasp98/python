# for graph_funcs
# vectors
# P=0, D1 = 1, D2 = 2, K = 3, Q = 4, H = 5
V = ["P", "D1", "D2", "K", "Q", "H"]
# edges
E = [
    ["P", "D1"], ["P", "D2"], ["D1", "D2"], ["P", "K"], ["P", "Q"], ["P", "H"],
    ["K", "Q"], ["K", "H"], ["Q", "H"]
]

# for graph_visualization
mapped_people = {
    0: "P",
    1: "D1",
    2: "D2",
    3: "K",
    4: "Q",
    5: "H"
}

mp_r = {
    "P": 0,
    "D1": 1,
    "D2": 2,
    "K": 3,
    "Q": 4,
    "H": 5
}

edges = [
    (mp_r["P"], mp_r["D1"]), (mp_r["P"], mp_r["D2"]),
    (mp_r["D1"], mp_r["D2"]), (mp_r["P"], mp_r["K"]),
    (mp_r["P"], mp_r["Q"]), (mp_r["P"], mp_r["H"]),
    (mp_r["K"], mp_r["Q"]), (mp_r["K"], mp_r["H"]),
    (mp_r["Q"], mp_r["H"])
]

bg_size = {
    "h_x": 13.38,
    "h_y": 10.39,
    "l_x": 5.38,
    "l_y": 5.6
}

pos = {
    0: (5, 5),
    1: (0, 5),
    2: (0, 10),
    3: (10, 10),
    4: (7.5, 5),
    5: (10, 0)
}
