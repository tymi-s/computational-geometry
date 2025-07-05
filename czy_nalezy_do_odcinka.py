
def czy_nalezy_do_odc(punkt,tab_pkt,param_prost):

    if (punkt[0]>=tab_pkt[0].x and punkt[0]<=tab_pkt[1].x  ):
        if(punkt[1  ] == param_prost[0]*punkt[0]+param_prost[1]): #czyli y punktu ==ax+b
            print(f"punkt ({punkt[0]},{punkt[1]}) nalezy do odcinka miedzy punktami ({tab_pkt[0].x}, {tab_pkt[0].y}),({tab_pkt[1].x}, {tab_pkt[1].y})")

    else:
        print(
            f"punkt ({punkt[0]},{punkt[1]}) NIE  nalezy do odcinka miedzy punktami ({tab_pkt[0].x}, {tab_pkt[0].y}),({tab_pkt[1].x}, {tab_pkt[1].y})")

