dic ={'samayapuram':1,'1_tollgate':2,'srirangam':3,'chinthamani':4,'cbs':5,'wb_road':6,'gandhi_market':7,'thillai_nagar':8,'tennur':9,'anna_nager':10,'padugai':11,'tmbs':12}
boarding=input('enter the starting station:').lower()
destination=input('enter the end station:').lower()
journey=int(input('enter 1.single journey 2.double journey:'))
if boarding in dic and destination in dic:
    t_price = abs(dic[destination] - dic[boarding])
    n_price = 0
    if t_price >= 2 and t_price < 4:
        n_price = 2 * 8
    elif t_price >= 4 and t_price < 6:
        n_price = 3 * 8
    elif t_price >= 6 and t_price < 8:
        n_price = 4 * 8
    elif t_price >= 8:
        n_price = 5 * 8
    if journey == 2:
        n_price *= 2
    print('-' * 30)
    print('Welcome to TRICHY METRO RAIL')
    print(f'Your journey {"double" if journey == 2 else "single"} journey')
    print(f'Your boarding point: {boarding}')
    print(f'Your destination point: {destination}')
    print(f'Fare: ₹{n_price}')
    print('Happy journey with our TMR..')
    print('-' * 30)

    start_station = boarding
    end_station = destination
    journey_type = "Double Journey" if journey == 2 else "Single Journey"
    fare = n_price

    import qrcode
    import random
    import string
    import matplotlib.pyplot as plt
    import numpy as np
    def generate_random_data(length=20):
        characters = string.ascii_letters + string.digits + string.punctuation
        random_data = ''.join(random.choice(characters) for _ in range(length))
        return random_data
    data = generate_random_data()
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_array = np.array(img)
    plt.figure(figsize=(1,3))

    

    plt.text(0.5, 0.7, "Welcome to TRICHY METRO RAIL", ha='left', va='bottom', fontsize=12, weight='bold')
    plt.text(0.5, 0.6, f"You journey: {journey_type}", ha='left', va='bottom', fontsize=12)
    plt.text(0.5, 0.5, f"Boarding Point: {start_station}", ha='left', va='bottom', fontsize=12)
    plt.text(0.5, 0.4, f"Destination Point: {end_station}", ha='left', va='bottom', fontsize=12)
    plt.text(0.5, 0.3, f"Fare: ₹{fare}", ha='left', va='bottom', fontsize=16, color='red')
    plt.text(0.5, 0.2, "Happy journey with our TMR!", ha='left', va='bottom', fontsize=12)


    plt.imshow(img_array, cmap='gray', extent=[-0.5,0.5,0,1])
    plt.axis('off')
    plt.show()

else:
    if destination != dic and boarding != dic:
        print(f'{'-' * 110}')
        print(f'sorry, sir/madam your boarding or destination point  is not available or your journey option is not available.')
        print(f'{'-' * 110}')
