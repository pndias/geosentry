import React from 'react';
import { Activity } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="main-header">
      <div className="header-info">
        <Activity size={20} className="pulse" />
        <span>Monitoramento Global em Tempo Real</span>
      </div>
      <div className="user-profile">
        <span>Sentinela do Sul Global</span>
        <div className="avatar">GS</div>
      </div>
    </header>
  );
};

export default React.memo(Header);
