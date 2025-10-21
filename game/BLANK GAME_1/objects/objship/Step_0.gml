if keyboard_check(vk_up) {motion_add(objship.image_angle + 90,0.2);}

if keyboard_check(vk_down) {motion_add(objship.image_angle - 90,0.2);}


if keyboard_check(vk_left) {image_angle += 4;}

if keyboard_check(vk_right) {image_angle -= 4;}


if keyboard_check_pressed(vk_space)
{
instance_create_layer(x,y,"Instances", obj_bullet)	
}
move_wrap(true, true, 10)