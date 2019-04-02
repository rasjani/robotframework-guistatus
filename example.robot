*** Settings ***
Library         GuiStatusKeywords
Suite Setup     Start Status UI
Suite Teardown  Stop Status UI

*** Test Cases ***
Start And Stop
  Status UI Log               GuiStatus Demo
  ${count}=                   Set Variable    50
  Status UI Progressbar       ${count}
  FOR   ${tick}   IN RANGE    ${count}
      Status UI Log           Processing ${tick}/${count}
      Status UI Action        step
  END
