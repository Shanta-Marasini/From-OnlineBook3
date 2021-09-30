# listt = [2,3,4,11,2,4,88,]
# listt.reverse()
# assert listt[0]<=listt[-1],'it is not sorted'

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'yellow'}

#switch light to next color of sequence
def switchLights(spotLight):
    for key in spotLight.keys():
        if spotLight[key] == 'green':
            spotLight[key] = 'yellow'
        elif spotLight[key] == 'yellow':
            spotLight[key] = 'red'
        elif spotLight[key] == 'red':
            spotLight[key] = 'green'
    #this function has a function that traffic in both streets can have
    #no red light in some conditions
    # resolve through assertion
    assert 'red' in spotLight.values(),'Neither light is red' + str(spotLight)

switchLights(mission_16th)

