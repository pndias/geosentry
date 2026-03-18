import React from 'react';
import { Activity } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="main-header">
      <div className="header-info">
        <Activity size={20} className="pulse" />
        <span>Real-Time Global Monitoring</span>
      </div>
      <div className="user-profile">
        <span>Global South Sentinel</span>
        <div className="avatar">GS</div>
      </div>
    </header>
  );
};

export default React.memo(Header);
