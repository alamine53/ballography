from io import BytesIO
import matplotlib.pyplot as plt
from urllib import request

def get_player_img(nba_id):
    img_url =  "https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/" + str(nba_id) +".png"
    url_response = request.urlopen(img_url)
    img = plt.imread(BytesIO(url_response.read()))
    return img

if __name__ == "__main__":
    
    # test the function
    img = get_player_img(202681) # Kyrie Irving
    plt.imshow(img)
    plt.axis('off')
    plt.show()