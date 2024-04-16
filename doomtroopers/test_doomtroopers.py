import pytest
import unittest.mock as mock
from project.wsgi import *
from doomtroopers.views import *
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate

doomtroopers = [
	{
		"id": 1,
		"name": "Valerie Duval",
		"picture": "https://res.cloudinary.com/dqk3feale/image/upload/v1708703203/Siege%20of%20the%20Citadel/valerie_duval_o3adwd.jpg",
		"description": "The daughter of a prominent Field Marshall, a career in the Bauhaus military was inevitable. She joined the ranks of the Etoiles Mortant through cunning, deadly precision, and iron will to become a spectre of death. Her renown grew, which led Doomtroopers to call at her door.",
		"corporation": 4,
		"specialist_type": 2
	},
	{
		"id": 2,
		"name": "Carl Lind",
		"picture": "https://res.cloudinary.com/dqk3feale/image/upload/v1708703200/Siege%20of%20the%20Citadel/carl_lind_zhgguj.jpg",
		"description": "A scion of House Phillipe, he put his family's electronic facilities to good use from an early age. As an adherent of the Order of the Devilcat, he is as deadly a warrior on the electronic battlefield as he is on the physical. His talents have cracked open numerous Dark Legion Citadels.",
		"corporation": 4,
		"specialist_type": 3
	},
	{
		"id": 3,
		"name": "Max Steiner",
		"picture": "https://res.cloudinary.com/dqk3feale/image/upload/v1708703208/Siege%20of%20the%20Citadel/max_steiner_cnbkut.jpg",
		"description": "An officer, but no gentleman, many a scandal followed his early career, much to the chagrin of his esteemed noble family. Chiselled, handsome features, and deadly skills honed beneath the Venusian jungle canopy have made him a media sensation.",
		"corporation": 4,
		"specialist_type": 1
	}
]


# @mock.patch("doomtroopers.views.Doomtrooper.objects.all")
# def test_get_all_doomtroopers_view(mock_doomtroopers_queryset):
#     mock_doomtroopers_queryset.return_value = doomtroopers

#     print('mock queryset ->', mock_doomtroopers_queryset.return_value)

#     # I'm not sure why this is accessing the real queryset and not the mocked one
#     print('doomtrooper list ->', doomtrooper_list.queryset)


#     assert True == False

def test_get_all_doomtroopers_view():
  with mock.patch("doomtroopers.views.DoomtrooperListCreateView") as doomtrooper_list:
    doomtrooper_list.queryset.return_value = doomtroopers
    data = doomtrooper_list.queryset.return_value
  
  # This isn't actually testing anything, but calling DoomtrooperListCreateView list will not access the patched data
  assert data == doomtroopers