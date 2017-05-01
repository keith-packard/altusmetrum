90
Name
Help;;help_end;;
ID
Name Fragment
NameFragment is a local device name. If a remote device requires a local name, a local device replies the local device name;;help_end;;
IDC_STATIC_NAME_FRAGMENT
HCI Baud Rate Index
The HCI Baud Rate Index is the baud rate index of the HCI UART.;;help_end;;
IDC_STATIC_HCI_BAUD_RATE_INDEX
H/W Flow Control
Set this parameter to enable UART H/W flow control(CTS).
If MCU not support flow control, this parameter need be set as disable to disable this function.
If  Operation Pattern choose Manual Pattern, then this parameter will be set as disable.;;help_end;;
IDC_STATIC_CTS_RTS_FLOW_CONTROL
Check Rx Data Interval
This parameter is used to set Check UART RX Data Interval.;;help_end;;
IDC_STATIC_CHECK_RX_DATA_INTERVAL
UART RX_IND
Enable / Disable UART RX IND ;;help_end;;
IDC_STATIC_UART_RX_IND
Operation Pattern
This parameter is used to set the operation pattern.;;help_end;;
IDC_STATIC_OPERATION_PATTERN
Configure Mode Timeout
This parameter is used to set BM77 configure mode timeout.;;help_end;;
IDC_STATIC_CONFIGURE_MODE_TIMEOUT
Power On Standby Time
The standby time duration after power on. device shall enter save power mode when time is up.
0x00~0xFE: Standby time parameters.
0xFF: Disable auto power_off function(enter S2 mode);;help_end;;
IDC_STATIC_POWER_ON_STANDBY_TIME
Disconnection Standby Time
The standby time duration after disconnection.
Device shall enter save power mode when time is up.
0x00~0xFE: Standby time parameters.
0xFF: Disable auto power_off function(enter S2 mode);;help_end;;
IDC_STATIC_REMOTE_DISCONNECT_STANDBY_TIME
Wakeup Externel MCU Wait Time
Waiting time duration to wake MCU up.;;help_end;;
IDC_STATIC_WAKEUP_EXTERNAL_MCU_WAIT_TIME
Wakeup Pin Option
This parameter is used to decide BLEDK3 can be waken up from shutdown mode by wakeup pin or not.;;help_end;;
IDC_STATIC_WAKEUP_PIN_OPTION
Bluetooth 4.0 BLE Security
This parameter is uesd to set BLE Security.;;help_end;;
IDC_STATIC_BLE_SECURITY
Trust Device Connection
This parameter is used to enable/disable trust (paired) device connection.;;help_end;;
IDC_STATIC_TRUST_DEVICE_CONNECTION
IO Capability
This parameter is used to config IO Capability;;help_end;;
IDC_STATIC_IO_CAPABILITY
BLE User Confirm Option
This parameter is used to enable/disable LE user confirm refer to passkey. And passkey must set 6 digits if enable.;;help_end;;
IDC_STATIC_BLE_USER_CONFIRM_OPTION
Passkey
The Passkey which is six byte ASCII code and be used in passkey confirm.;;help_end;;
IDC_STATIC_PASSKEY
LE Secure Connections
This parameter is used to enable/disable LE Secure Connections.;;help_end;;
IDC_STATIC_LE_SECURE_CONNECTIONS
Link Manager Version
This parameter is used to choose Link Manager Version is BT4.0 or BT4.2.;;help_end;;
IDC_STATIC_LINK_MANAGER_VERSION
Data Length Extension
This parameter is used to enable/disable Data Length Extension.;;help_end;;
IDC_STATIC_DATA_LENGTH_EXTENSION
 eFlash Footprint
The 16 ASCII characters for the customers' version control code. The download tool can check by this code and reject to download the eFlash if it's mismatch.;;help_end;;
IDC_STATIC_FOOTPRINT
Link Quality Detection
Enable/Disable link quality detection.
The RF_Tx_Power_Control_feature will be disabled if Enable this parameter.;;help_end;;
IDC_STATIC_LINK_QUALITY_DETECTION
RSSI Normal Threshold
This parameter is used to set RSSI normal threshole value;;help_end;;
IDC_STATIC_RSSI_NORMAL_THRESHOLD
RSSI Weak Threshold
This parameter is used to set RSSI weak threshole value;;help_end;;
IDC_STATIC_RSSI_WEAK_THRESHOLD
Battery Detection  Interval
Thie parameter is uesd to set battery detection  interval;;help_end;;
IDC_STATIC_BATTERY_DETECTION
High Battery Level
High battery level;;help_end;;
IDC_STATIC_HIGH_BATTERY_LEVEL
Normal Battery Level
This parameter is defined a normal voltage value of a battery. When the voltage is lower than this value,the device will start low battery warring.;;help_end;;
IDC_STATIC_NORMAL_BATTERY_LEVEL
Low Battery Level
This parameter is defined a low voltage value of a battery. When the voltage is lower than this value, the device will shutdown.;;help_end;;
IDC_STATIC_LOW_BATTERY_LEVEL
Dangerous Battery Level
Dangerout battery level;;help_end;;
IDC_STATIC_DANGEROUS_BATTERY_LEVEL
Low Battery Into Shutdown Time
This parameter is used to set the waiting time befor enter into shutdown mode if low battery happens.
(0x00: Disable enter into shutdown mode when low battery happens);;help_end;;
IDC_STATIC_LOW_BATTERY_INTO_POWER_DOWN_TIME
RF Class
The RF_Class is the RF class type.;;help_end;;
IDC_STATIC_RF_CLASS
P36
Set the function mapping to the GPIO P3_6;;help_end;;
IDC_STATIC_P36
P10
Set the function mapping to the GPIO P1_0;;help_end;;
IDC_STATIC_P10
P00
Set the function mapping to the GPIO P0_0;;help_end;;
IDC_STATIC_P00
P31
Set the function mapping to the GPIO P3_1;;help_end;;
IDC_STATIC_P31
P32
Set the function mapping to the GPIO P3_2;;help_end;;
IDC_STATIC_P32
P33
Set the function mapping to the GPIO P3_3;;help_end;;
IDC_STATIC_P33
P34
Set the function mapping to the GPIO P3_4;;help_end;;
IDC_STATIC_P34
P07
Set the function mapping to the GPIO P0_7;;help_end;;
IDC_STATIC_P07
P11
Set the function mapping to the GPIO P1_1;;help_end;;
IDC_STATIC_P11
P22
Set the function mapping to the GPIO P2_2;;help_end;;
IDC_STATIC_P22
P24
Set the function mapping to the GPIO P2_4;;help_end;;
IDC_STATIC_P24
P35
Set the function mapping to the GPIO P3_5;;help_end;;
IDC_STATIC_P35
P12
Set the function mapping to the GPIO P1_2;;help_end;;
IDC_STATIC_P12
P13
Set the function mapping to the GPIO P1_3;;help_end;;
IDC_STATIC_P13
P16
Set the function mapping to the GPIO P1_6;;help_end;;
IDC_STATIC_P16
P17
Set the function mapping to the GPIO P1_7;;help_end;;
IDC_STATIC_P17
RF Active IND MCU Include
This parameter is used to choose the indication type of RF active time.;;help_end;;
IDC_STATIC_RF_ACTIVE_IND_MCU_INCLUDE
LE Connection Parameter Update Request
The LE Connection Setting will be assigned by Remote if select Disable.
It will sent update request if select Enable.;;help_end;;
IDC_STATIC_LE_CONNECTION_PARAMETER_UPDATE
Min LE Connection Interval
This parameter is used to set LE min connection interval;;help_end;;
IDC_STATIC_MIN_LE_CONNECTION_INTERVAL
Max LE Connection Interval
This parameter is used to set LE max connection interval;;help_end;;
IDC_STATIC_MAX_LE_CONNECTION_INTERVAL
LE Slave Latency
This parameter is used to set LE slave latency;;help_end;;
IDC_STATIC_LE_SLAVE_LATENCY
LE Supervision Timeout
This parameter is used to set LE supervision timeout ;;help_end;;
IDC_STATIC_LE_SUPERVISION_TIMEOUT
LE Fast Advertising Interval
This parameter is uesd to set LE fast advertising interval;;help_end;;
IDC_STATIC_LE_FAST_ADVERTISING_INTERVAL
LE Reduced Power Advertising Interval
This parameter is uesd to set LE reduced power advertising interval;;help_end;;
IDC_STATIC_LE_REDUCED_POWER_ADVERTISING
LE Fast Advertising Timeout
This parameter is uesd to set LE fast advertising timeout value;;help_end;;
IDC_STATIC_LE_FAST_ADVERTISING_TIMEOUT
Power On LE Reduced Power Advertising Timeout
This parameter is uesd to show Power On LE Reduced Power Advertising timeout value.
Power On LE Reduced Power Advertising timeout = Power on Standby Time - LE Fast Advertising Timeout.;;help_end;;
IDC_STATIC_POWER_ON_LE_REDUCED_POWER_ADVERTISING_TIMEOUT
Disconnection LE Reduced Power Advertising Timeout
This parameter is uesd to show Disconnection LE Reduced Power Advertising Timeout value.
Disconnection LE Reduced Power Advertising Timeout  = Disconnection Standby Time - LE Fast Advertising Timeout;;help_end;;
IDC_STATIC_DISCONNECTION_LE_REDUCED_POWER_ADVERTISING_TIMEOUT
Advertising Prefered Power Level
Prefered Tx power level when advertising.;;help_end;;
IDC_STATIC_ADVERTISING_TX_POWER_LEVEL
Connected Prefered Power Level
Prefered Tx power level when connected.;;help_end;;
IDC_STATIC_CONNECTED_TX_POWER_LEVEL
Advertising Data Setting
This parameter is uesd to set advertising data.
Reference RSSI - This value represents the measured strength of the beacon from one meter away and is used during ranging.;;help_end;;
IDC_STATIC_ADVERTISING_DATA_SETTING
Scan Response Data Setting
This parameter is uesd to set scan response data;;help_end;;
IDC_STATIC_SCAN_RESPONSE_DATA_SETTING
Type
This is the LED display method.;;help_end;;
IDC_STATIC_LED_TYPE
On Duration
This the LED on time for flash.;;help_end;;
IDC_STATIC_LED_ON_TIME
Off Duration
This the LED off time for flash.;;help_end;;
IDC_STATIC_LED_OFF_TIME
Count
This is the number of the flash times for a round.;;help_end;;
IDC_STATIC_LED_COUNT
Interval
This is the time interval for a round.;;help_end;;
IDC_STATIC_LED_INTERVAL
Type
This is the LED display method.;;help_end;;
IDC_STATIC_LED_TYPE
On Duration
This the LED on time for flash.;;help_end;;
IDC_STATIC_LED_ON_TIME
Off Duration
This the LED off time for flash.;;help_end;;
IDC_STATIC_LED_OFF_TIME
Count
This is the number of the flash times for a round.;;help_end;;
IDC_STATIC_LED_COUNT
Interval
This is the time interval for a round.;;help_end;;
IDC_STATIC_LED_INTERVAL
Type
This is the LED display method.;;help_end;;
IDC_STATIC_LED_TYPE
On Duration
This the LED on time for flash.;;help_end;;
IDC_STATIC_LED_ON_TIME
Off Duration
This the LED off time for flash.;;help_end;;
IDC_STATIC_LED_OFF_TIME
Count
This is the number of the flash times for a round.;;help_end;;
IDC_STATIC_LED_COUNT
Type
This is the LED display method.;;help_end;;
IDC_STATIC_LED_TYPE
On Duration
This the LED on time for flash.;;help_end;;
IDC_STATIC_LED_ON_TIME
Off Duration
This the LED off time for flash.;;help_end;;
IDC_STATIC_LED_OFF_TIME
Count
This is the number of the flash times for a round.;;help_end;;
IDC_STATIC_LED_COUNT
Interval
This parameter is uesd to set LED warning time interval if low battery happens;;help_end;;
IDC_STATIC_LOW_BATTERY_LED_INTERVAL
LED Brightness
LED brightness setting.;;help_end;;
IDC_STATIC_LED1_BRIGHTNESS
Beacon Feature
Enable/Disable Beacon function;;help_end;;
IDC_STATIC_BEACON_FEATURE
Beacon Admin Mode
Enable/Disable Beacon admin mode;;help_end;;
IDC_STATIC_BEACON_ADMIN_MODE
Beacon Admin Timeout
This parameter is used to configure Beacon admin timeout value
0x00: Disable Beacon Admin Feature;;help_end;;
IDC_STATIC_BEACON_ADMIN_TIMEOUT
Beacon In Connection
If Beacon In Connect is Enable, beacon advertising will stop when LE connection is established.;;help_end;;
IDC_STATIC_BEACON_IN_CONNECTION
Beacon Advertising Interval
This parameter is used to confirue advertising interval for Beacon using;;help_end;;
IDC_STATIC_BEACON_ADVERTISING_INTERVAL
Beacon Advertising Data Length
This paraeter is used to configure advertising data len for Beacon using;;help_end;;
IDC_STATIC_BEACON_ADVERTISING_DATA_LENGTH
Beacon Advertising Data
This paraeter is used to configure advertising data for Beacon using;;help_end;;
IDC_STATIC_BEACON_ADVERTISING_DATA
Beacon Secret Key
This parameter is used to config Secret key for Beacon Admin usage;;help_end;;
IDC_STATIC_BEACON_SECRET_KEY
