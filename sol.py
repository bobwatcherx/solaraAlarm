from solara import *
import time
import threading

# NOW I WILL SHOW DIALOG IF TIME IS 0 SECONDS
import reacton.ipyvuetify as v



@solara.component
def Page():
	# NOW I CREATE STATE
	alarmtime,set_alarmtime = use_state(5)
	timing,set_timing = use_state(alarmtime)
	showdialog,set_showdialog = use_state(False)
	alarm_active = False	


	def changeduration(value):
		print("you select",value)
		set_alarmtime(value)

	def setalarm():
		nonlocal alarm_active
		if not alarm_active:
			alarm_active = True
			threading.Thread(target=startalarm).start()

	def startalarm():
		nonlocal alarm_active
		# THIS alarmtime will increment every 1 seconds
		for i in range(alarmtime,0,-1):
			time.sleep(1)
			set_alarmtime(i - 1)

		# DISABLE ALARM IF 0 seconds
		alarm_active = False
		print("YOU TIME !!!!")
		# AND SHOW DIALOG
		set_showdialog(True)





	with Column(margin=10):
		Markdown(f"{alarmtime} Seconds",
			style={"font-size":"30px"}
			),
		Select(
			label="Select Yout time",
			value=timing,
			# NOW IF YOU CAHANGE THEN UPDATE set_timing
			on_value=changeduration,
			values=[5,4,3,2,1]
			),
		Button("Set Alarm",
			color="blue",
			on_click=setalarm
			)
		# AND NOW I WILL CREATE DIALOG HERE
		with v.Dialog(
			v_model=showdialog,
			persistent=True,
			on_v_model=set_showdialog):
			with Card():
				Markdown("alert TIME",
					style={"font-size":"30px","color":"red"}
					)
				Button("close",
					color="red",
					on_click=lambda:set_showdialog(False)
					)
