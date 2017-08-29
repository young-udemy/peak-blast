from models import MineField


def find_big_bangs(mines):
    if not mines:
        return []

    mine_field = MineField(mines)

    bangs = []
    for mine in mines:
        bangs += mine_field.get_bang_progression(mine)

    sorted_bangs = sorted(bangs,
                          key=lambda b: (-b.mine_count, b.starter.x_coord, b.starter.y_coord))
    max_explosion_count = sorted_bangs[0].mine_count

    big_bangs = []
    for bang in sorted_bangs:
        if bang.mine_count < max_explosion_count:
            break
        big_bangs.append(bang)

    return big_bangs
