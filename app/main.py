import bottle
import os

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': 'green',
        'head': head_url
    }

@bottle.post('/start')
def start():
    data = bottle.request.json

    # THIS IS THE DATA WE RECEIVE: 
    # {
    #     "game": "hairy-cheese",
    #     "mode": "classic",
    #     "turn": 0,
    #     "height": 20,
    #     "width": 30,
    #     "snakes": [
    #         <Snake Object>, <Snake Object>, ...
    #     ],
    #     "food": []
    # }

    return {
        'taunt': 'Medusa snake go!'
    }

@bottle.post('/move')
def move():
    data = bottle.request.json
    move_decision = 'north'

    # THIS IS THE DATA WE RECEIVE: 
    # {
    #     "game": "hairy-cheese",
    #     "mode": "classic",
    #     "turn": 4,
    #     "height": 20,
    #     "width": 30,
    #     "snakes": [
    #         <Snake Object>, <Snake Object>, ...
    #     ],
    #     "food": [
    #         [1, 2], [9, 3], ...
    #     ]
    # }

    return {
        'move': move_decision,
        'taunt': 'MEDUSA ATTACK!'
    }

@bottle.post('/end')
def end():
    data = bottle.request.json
    
    # THIS IS THE DATA WE RECEIVE: 
    # {
    #     "game": "hairy-cheese",
    #     "mode": "classic",
    #     "turn": 4,
    #     "height": 20,
    #     "width": 30,
    #     "snakes": [
    #         <Snake Object>, <Snake Object>, ...
    #     ],
    #     "food": [
    #         [1, 2], [9, 3], ...
    #     ]
    # }

    return {
        'taunt': 'Good game all!'
    }

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
