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
      print("No listings at the moment.")
      


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

  def __repr__(self):
    if self.is_museum:
      return("This client is a museum.")
    else:
      return("This client is a person.")   
      
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
    
      
print("\n\"VENEER\" CREATED AS MARKET")
veneer = Marketplace() 

print("\"EDYTTA\" CREATED AS CLIENT")
edytta = Client("Edytta Halpirt", "None", False)

print("\"GIRL WITH MANDOLIN\" CREATED AS ART OBJECT")
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)
print("\nCurrent artwork information:")
print(girl_with_mandolin)
print("\nCurrent market listings:")
veneer.show_listings()


print("\nArtwork uploaded for sale.")
print("The price is \"$6 MILLION\" U.S. dollars.")
edytta.sell_artwork(girl_with_mandolin, "$6M(USD)")

print("\nCurrent market listings:")
veneer.show_listings()

print("\nWaiting for client.")
print("\nA client arrived.")
print("Her name is \"The MOMA\".")
moma = Client("The MOMA", "New York", True)
print(moma)
print("Artwork purchased by The Moma.")
moma.buy_artwork(girl_with_mandolin)

print("\nCurrent artwork information:")
print(girl_with_mandolin)
print("\nCurrent market listings:")
veneer.show_listings()
