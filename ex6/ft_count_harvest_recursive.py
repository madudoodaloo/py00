# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: masilva- <masilva-@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/18 15:04:11 by masilva-          #+#    #+#              #
#    Updated: 2026/08/18 15:04:11 by masilva-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def recursive_print(total: int, curr: int) -> None:
	if (curr > total):
		print("Harvest time!")
		return
	print("Day", curr)
	recursive_print(total, curr + 1)

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	recursive_print(days, 1)	

ft_count_harvest_recursive()

