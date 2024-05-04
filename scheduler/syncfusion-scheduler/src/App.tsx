import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { ScheduleComponent, Day, Week, WorkWeek, Month, Agenda, Inject, ActionEventArgs } from '@syncfusion/ej2-react-schedule';

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/schedule');
        const data = await response.json();
        setEvents(data);
      } catch (error) {
        console.error('Failed to fetch data:', error);
      }
    };
  
    fetchData();
  }, []);

  const onActionComplete = async (args: ActionEventArgs) => {
    if (args.requestType === "eventCreated") {
      if (args.addedRecords && args.addedRecords.length > 0) {
        for (const record of args.addedRecords) {
          await fetch('http://127.0.0.1:8000/schedule', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(record),
          });
        }
      }
    }
  
    if (args.requestType === "eventChanged") {
      if (args.changedRecords && args.changedRecords.length > 0) {
        for (const record of args.changedRecords) {
          await fetch(`http://127.0.0.1:8000/schedule/${record.Id}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(record),
          });
        }
      }
    }
  
    if (args.requestType === "eventRemoved") {
      if (args.deletedRecords && args.deletedRecords.length > 0) {
        for (const record of args.deletedRecords) {
          await fetch(`http://127.0.0.1:8000/schedule/${record.Id}`, {
            method: 'DELETE',
          });
        }
      }
    }
  }


  return (
    <ScheduleComponent allowResizing={true} allowDragAndDrop={ true } eventSettings={{ dataSource: events }} actionComplete={onActionComplete}>
      <Inject services={[Day, Week, WorkWeek, Month, Agenda]}/>
    </ScheduleComponent>
  );
}

export default App;