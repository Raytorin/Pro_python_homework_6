stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def max_sales(stats_sales):
    max_stats = max(stats_sales, key=stats.get)
    return max_stats


if __name__ == '__main__':
    max_sales(stats)
