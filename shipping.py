#Calculate cost of ground shipping
def ground_shipping(weight):
  if weight < 2:
    price_per_pound = 1.5
  elif weight <= 6:
   price_per_pound = 3
  elif weight <= 10:
    price_per_pound = 4
  else:
    price_per_pound = 4.75

  return (weight * price_per_pound) + 20
  
#Premium shipping price
shipping_cost_premium = 125

#Calculate drone price
def drone_shipping(weight):
  if weight < 2:
    price_per_pound = 4.50
  elif weight <= 6:
   price_per_pound = 9
  elif weight <= 10:
    price_per_pound = 12
  else:
    price_per_pound = 14.25

  return (weight * price_per_pound)


def cheapest_method(weight):
    ground = ground_shipping(weight)
    premium = shipping_cost_premium
    drone = drone_shipping(weight)

    if ground < premium and ground < drone:
      method = 'Stardard Ground'
      cost = ground
    elif premium < ground and premium < drone:
      method = 'Premium Ground'
      cost = premium
    else:
      method = 'Drone'
      cost = drone

    print(
      'The cheapest option avaliable is $%.2f with %s shipping'
      %(cost, method)
    )

cheapest_method(4.8)
cheapest_method(41.5)



    
