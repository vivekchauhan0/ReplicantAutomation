#!/usr/bin/env python
import asyncio
import websockets
import traceback
import requests
import unittest
import pytest
import time
from Automation.WebSocketAutomation.mainWebSocketTestRunner import _data

sendMessages = {'help' : "help"
                }

URL = _data['URL']
if URL == 'TEST':
    URL = 'ws://192.168.1.86:4444'
if URL == 'PROD':
    URL = 'wss://chatbot-challenge.dev.replicant.ai'
baselineReceivedMessage = {}

# Test 1
@pytest.mark.asyncio
async def test_greeting():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                assert "Greetings, friend! Type" in greeting

            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 2
@pytest.mark.asyncio
async def test_incorrect_message():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("hello")

                greeting = await websocket.recv()
                print(greeting)

                assert "I'm sorry, I don't understand what you mean." == greeting

                #assert response.status_code == 200
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 3
@pytest.mark.asyncio
async def test_help_messaage():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                assert "I am a reminder bot, here to help you get organized. Here are some of the things you can ask me to do" in greeting

                #assert response.status_code == 200
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 4
@pytest.mark.asyncio
async def test_show_all_reminders_with_no_reminders_set():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("show all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "You have no reminders." in greeting
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 5
@pytest.mark.asyncio
async def test_clear_all_reminders_with_no_reminders_set():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("clear all reminders")

                greeting = await websocket.recv()
                print(greeting)

                # This is a bug
                # a) "Clear reminder" is not in contract and  it should say, "I'm sorry, I don't understand what you mean."
                # b) "Clear all reminders" should say, you do not have nay reminders, if there are no reminders
                assert "You have no reminders." in greeting
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 6
@pytest.mark.asyncio
async def test_add_a_reminders_with_no_reminders_set():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("remind me to make dinner in 5 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to make dinner in 300 seconds." in greeting
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 7
@pytest.mark.asyncio
async def test_list_reminders_with_one_reminders_set():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("remind me to make dinner in 5 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to make dinner in 300 seconds." in greeting

                await websocket.send("show all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "make dinner" in greeting
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 8
@pytest.mark.asyncio
async def test_list_reminders_with_two_reminders_set():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("remind me to make dinner in 5 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to make dinner in 300 seconds." in greeting

                await websocket.send("remind me to take out trash in 20 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to take out trash in 1200 seconds." in greeting

                await websocket.send("show all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "make dinner" in greeting
                assert "take out trash" in greeting
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 9
@pytest.mark.asyncio
async def test_reminder_time_after_sleep_with_one_reminders():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("remind me to make dinner in 5 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to make dinner in 300 seconds." in greeting

                # Wait for 60 Seconds and validate the time must be 240 seconds
                time.sleep(60)
                await websocket.send("show all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "make dinner" in greeting
                #Validating if the the bot waited for 240 seconds
                assert "240" in greeting
            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 10
@pytest.mark.asyncio
async def test_remove_list_reminders_with_two_reminders_set():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("remind me to make dinner in 5 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to make dinner in 300 seconds." in greeting

                await websocket.send("remind me to take out trash in 20 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to take out trash in 1200 seconds." in greeting

                await websocket.send("show all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "make dinner" in greeting
                assert "take out trash" in greeting

                # Now remove reminder 1

                await websocket.send("clear reminder 2")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will not remind you to" in greeting


            ############################################################

    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

# Test 11
@pytest.mark.asyncio
async def test_remove_all_reminder_with_two_reminders_set():
    try:
            uri = URL
            async with websockets.connect(uri) as websocket:
                # Wait for the first message
                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("help")

                greeting = await websocket.recv()
                print(greeting)

                await websocket.send("remind me to make dinner in 5 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to make dinner in 300 seconds." in greeting

                await websocket.send("remind me to take out trash in 20 minutes.")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I will remind you to take out trash in 1200 seconds." in greeting

                await websocket.send("show all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "make dinner" in greeting
                assert "take out trash" in greeting

                # Now remove reminder 1

                await websocket.send("clear all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "Ok, I have cleared all of your reminders." in greeting

                await websocket.send("show all reminders")

                greeting = await websocket.recv()
                print(greeting)

                assert "You have no reminders." in greeting


            ############################################################
    except Exception:
            print("Error in processing test_greeting")
            print(traceback.format_exc())

" Another scenario : Connection lost. Goodbye!"