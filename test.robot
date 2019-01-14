*** Settings ***
Library   GuiStatusKeywords
Suite Setup   Start Status UI
Suite Teardown  Stop Status UI

*** Test Cases ***
Start And Stop
  Status UI Log   Hello World
  Sleep   5 seconds
