# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: masilva- <masilva-@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/18 14:27:20 by masilva-          #+#    #+#              #
#    Updated: 2026/08/18 14:27:20 by masilva-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day1 = input("Day 1 harvest: ")
	day2 = input("Day 2 harvest: ")
	day3 = input("Day 3 harvest: ")
	total = int(day1) + int(day2) + int(day3)
	print("Total harvest:", total)

ft_harvest_total()