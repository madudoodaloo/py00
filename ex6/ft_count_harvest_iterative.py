# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: masilva- <masilva-@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/18 15:03:54 by masilva-          #+#    #+#              #
#    Updated: 2026/08/18 15:03:54 by masilva-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
	days = int(input("Days until harvest: "))
	for i in range(1, days + 1):
		print("Day", i)
	print("Harvest time!")


