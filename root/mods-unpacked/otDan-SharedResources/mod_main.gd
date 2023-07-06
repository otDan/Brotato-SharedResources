extends Node

const MOD_NAME = "otDan-SharedResources"

var dir = ""
var translations_dir = ""
var extensions_dir = ""


func _init(_mod_loader):
	ModLoaderLog.info("Init", MOD_NAME)

	dir = ModLoaderMod.get_unpacked_dir() + MOD_NAME + "/"
	translations_dir = dir + "translations/"
	extensions_dir = dir + "extensions/"

	_install_translations()
	_install_script_extensions()
	_add_child_classes()


func _ready():
	ModLoaderLog.success("Loaded", MOD_NAME)


func _disable():
	pass


func _install_translations() -> void:
	pass


func _install_script_extensions():
	pass


func _add_child_classes():
	pass
