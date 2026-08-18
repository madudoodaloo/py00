# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: masilva- <masilva-@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/18 14:41:37 by masilva-          #+#    #+#              #
#    Updated: 2026/08/18 14:41:37 by masilva-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	days = input("Days since last watering: ")
	if int(days) > 2 :
		print("Water the plants!")
	else :
		print("Plants are fine")

ft_water_reminder()