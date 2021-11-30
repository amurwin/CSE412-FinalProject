from django.shortcuts import render

from pokemondb.models import Pokemon, appearance, pokeMove, Move, pokeAbility, Ability


def all_pokemon(request):
    name_obj = Pokemon.objects
    
    context = {
        "pokemons": name_obj,
    }

    return render(request, "pokemon_detail.html", context)


def poke_detail(request, pk):
    poke_obj = Pokemon.objects.get(pk=pk)

    form_obj = appearance.objects.filter(unique=poke_obj.id)

    poke_move_obj = pokeMove.objects.filter(pokemon=poke_obj.name)

    move_obj = Move.objects.filter(name__in=[move.move for move in poke_move_obj.all()])

    poke_ability_obj = pokeAbility.objects.filter(name=poke_obj.name)

    ability_obj = Ability.objects.filter(name__in=[ability.ability for ability in poke_ability_obj.all()])

    context = {
        "pokemon": poke_obj,

        "details": form_obj,

        "moves": move_obj,

        "abilities": ability_obj,
    }

    return render(request, "specific_pokemon.html", context)


def all_abilities(request):
    ability_obj = Ability.objects

    context = {
        "abilities": ability_obj,
    }

    return render(request, "abilities.html", context)


def ability_detail(request, pk):
    ability_obj = Ability.objects.get(pk=pk)

    poke_ability_obj = pokeAbility.objects.filter(ability=ability_obj.name)

    poke_obj = appearance.objects.filter(form__in=[ability.name.name for ability in poke_ability_obj.all()])

    context = {
        "ability": ability_obj,

        "pokemons": poke_obj,
    }

    return render(request, "specific_ability.html", context)


def all_moves(request):
    move_obj = Move.objects

    context = {
        "moves": move_obj,
    }

    return render(request, "moves.html", context)


def move_detail(request, pk):
    move_obj = Move.objects.get(pk=pk)

    poke_move_obj = pokeMove.objects.filter(move=move_obj.name)

    poke_obj = appearance.objects.filter(form__in=[move.pokemon.name for move in poke_move_obj.all()])

    context = {
        "move": move_obj,

        "pokemons": poke_obj,
    }

    return render(request, "specific_move.html", context)
