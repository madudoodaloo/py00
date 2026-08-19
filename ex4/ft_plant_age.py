# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: masilva- <masilva-@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/18 14:37:03 by masilva-          #+#    #+#              #
#    Updated: 2026/08/18 14:37:03 by masilva-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() -> None:
	age = input("Enter plant age in days: ")
	if int(age) > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
