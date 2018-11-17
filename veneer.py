import time

class Art:
  
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  
  def __repr__(self):
    return ('%s. "%s". %s, %s. %s, %s.' % (self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location))
  


class Marketplace:
  
  def __init__(self, listings = []):
    self.listings = listings
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    
  def show_listings(self):
    if self.listings:
      for listing in self.listings:
        print(listing)
    else:
      print("NO LISTINGS AT THE MOMENT")
      


class Listing:
  
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
    
  def __repr__(self):
    return ("%s / %s" % (self.art.title, self.price))
    
  
  
class Client:
  
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if self.is_museum:
      self.location = location
    else:
      self.location = "Private Collection"
      
  def sell_artwork(self, artwork, price):
    if self != artwork.owner:
      print("OWNERSHIP ALERT")
    this_listing = Listing(artwork, price, self)
    veneer.add_listing(this_listing)
    
  def buy_artwork(self, artwork):
    if self == artwork.owner:
      print("OWNERSHIP ALERT")
    for listing in veneer.listings:
      if listing.art == artwork:
        artwork.owner = self
        veneer.remove_listing(listing)
    
      
print("CREATING \"VENEER\"...\n")
veneer = Marketplace() 
time.sleep(2)

print("GENERATING \"EDYTTA\" AS CLIENT...\n")
edytta = Client("Edytta Halpirt", "None", False)
time.sleep(1.5)

print("INITIALIZATION OF \"GIRL WITH MANDOLIN\" AS ART OBJECT...\n\n")
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)
time.sleep(3)

print("ITS PARAMETERS:\n")
time.sleep(0.3)
print(girl_with_mandolin)
time.sleep(5)

print("\n\n\n\nUploading artwork for sale.")
time.sleep(2)
print("The price is")
time.sleep(0.2)
print("$6 MILLION")
time.sleep(0.2)
print("U.S. dollars.\n\n")
time.sleep(3)
edytta.sell_artwork(girl_with_mandolin, "$6M(USD)")

print("PRINTING CURRENT MARKET...\n")
time.sleep(0.5)
veneer.show_listings()
time.sleep(1)

print("Waiting for client...\n\n")
time.sleep(3)
print("Still waiting... ...\n\n\n\n")
time.sleep(7)
print("CLIENT ARRIVED.\n")
time.sleep(1)
print("HER NAME IS MOMA.")
moma = Client("The MOMA", "New York", True)
time.sleep(1)

print("MOMA BUYING ARTWORK...")
moma.buy_artwork(girl_with_mandolin)
time.sleep(2)
print("\nPURCHASE COMPLETE.")
time.sleep(1)

print("\nREFRESHING MARKET INFORMATION...")
time.sleep(0.7)
print("REFRESH COMPLETE.")
print(girl_with_mandolin)
time.sleep(0.3)
print("CURRENT MARKET:")
veneer.show_listings()
