extends MyMenuButtonParent

signal value_toggled(mod, state)

onready var label = $MarginContainer/HBoxContainer/ScrollContainer/Label
onready var amount = $MarginContainer/HBoxContainer/Amount


func _ready() -> void:
	var _error_focus = connect("focus_entered", self, "on_focus_entered")
	var _error_press = connect("pressed", self, "on_pressed")
	var _error_mouse = connect("mouse_entered", self, "on_mouse_entered")


func set_info(mod: String, item_amount: int):
	label.text = mod
	amount.text = "[%s]" % str(item_amount)


func on_focus_entered():
	.on_focus_entered()
	label.scrolling = true
	label.add_color_override("font_color", Color.black)
	amount.add_color_override("font_color", Color.black)


func _on_ValueToggle_toggled(button_pressed):
	emit_signal("value_toggled", label.text, button_pressed)


func _on_ValueToggle_focus_exited():
	label.scrolling = false
	label.add_color_override("font_color", Color.white)
	amount.add_color_override("font_color", Color.white)
