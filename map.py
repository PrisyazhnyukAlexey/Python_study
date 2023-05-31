#
# # python
import pygame
#
# # инициализируем pygame
pygame.init()
#
# # устанавливаем размер экрана
screen = pygame.display.set_mode((1200, 600))
#
# # загружаем карту офиса
office_map = pygame.image.load('office-map.jpg')
#
# # создаем текстовые надписи для каждого отдела
font = pygame.font.Font(None, 50)
marketing_text = font.render("Отдел маркетинга", True, (255, 255, 255))
hr_text = font.render("HR отдел", True, (255, 255, 255))
sales_text = font.render("Отдел продаж", True, (255, 255, 255))
development_text = font.render("Отдел разработки", True, (255, 255, 255))
accounting_text = font.render("Бухгалтерия", True, (255, 255, 255))

# # настраиваем координаты и размеры каждой текстовой надписи
marketing_rect = marketing_text.get_rect()
marketing_rect.x, marketing_rect.y = 445, 307
hr_rect = hr_text.get_rect()
hr_rect.x, hr_rect.y = 127, 81
sales_rect = sales_text.get_rect()
sales_rect.x, sales_rect.y = 10, 10
development_rect = development_text.get_rect()
development_rect.x, development_rect.y = 450, 160
accounting_rect = accounting_text.get_rect()
accounting_rect.x, accounting_rect.y = 570, 400
#
# # основной цикл приложения
while True:
    # обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#     # отрисовываем карту офиса на экране
    screen.blit(office_map, (0, 0))

#     # отрисовываем текстовые надписи для каждого отдела на экране
    screen.blit(marketing_text, marketing_rect)
    screen.blit(hr_text, hr_rect)
    screen.blit(sales_text, sales_rect)
    screen.blit(development_text, development_rect)
    screen.blit(accounting_text, accounting_rect)
#
#     # обновляем экран
    pygame.display.update()