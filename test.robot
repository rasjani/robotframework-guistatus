*** Settings ***
Library   GuiStatusKeywords
Suite Setup   Start Status UI
Suite Teardown  Stop Status UI

*** Test Cases ***
Start And Stop
  Status UI Log   Hello World
  FOR   ${tick}   IN RANGE  100
      Status UI Log   Processing ${tick}/100
      Status UI Action  step
  END
  Sleep   5 seconds
