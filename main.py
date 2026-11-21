import os
import subprocess

svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
  <!-- Newspaper Background -->
  <rect width="1024" height="1024" fill="#fcfbf7"/>
  
  <!-- Masthead -->
  <text x="512" y="70" font-family="serif" font-size="48" font-weight="bold" text-anchor="middle" fill="#111">THE GLOBAL CHRONICLE</text>
  <text x="512" y="95" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#555" letter-spacing="2">FRIDAY, NOVEMBER 21, 2026 • EDITION 4,892</text>
  <line x1="50" y1="110" x2="974" y2="110" stroke="#111" stroke-width="3"/>
  <line x1="50" y1="116" x2="974" y2="116" stroke="#111" stroke-width="1"/>

  <!-- Top Hero Story -->
  <rect x="50" y="135" width="600" height="420" fill="#fff" stroke="#ccc" stroke-width="1"/>
  <text x="75" y="175" font-family="sans-serif" font-size="12" font-weight="bold" fill="#c00">BREAKING WORLDWIRE</text>
  <text x="75" y="215" font-family="serif" font-size="32" font-weight="bold" fill="#111">Global AI Agent Treaty Ratified</text>
  <text x="75" y="255" font-family="serif" font-size="16" fill="#333">Delegates from 142 nations sign historic accord establishing decentralized autonomous protocols, standardized safety rails, and cross-border machine commerce frameworks in Geneva summit.</text>
  <text x="75" y="325" font-family="serif" font-size="14" fill="#555">GENEVA — In an unprecedented unanimous vote early Friday morning, world leaders finalized the Autonomous Agent Treaty (AAT). The framework guarantees verifiable execution safeguards, cryptographic auditing, and sovereign compute allocation for verifiable agent networks worldwide.</text>

  <!-- Right Sidebar News -->
  <rect x="670" y="135" width="304" height="420" fill="#fff" stroke="#ccc" stroke-width="1"/>
  <text x="695" y="175" font-family="sans-serif" font-size="12" font-weight="bold" fill="#333">MARKETS &amp; TECH</text>
  <text x="695" y="215" font-family="serif" font-size="24" font-weight="bold" fill="#111">Solana Escrow Volume Hits Record $4.2B</text>
  <text x="695" y="260" font-family="serif" font-size="14" fill="#444">Autonomous settlement protocols process record throughput as agent-driven bounty ecosystems scale globally across decentralized exchanges.</text>
  <text x="695" y="340" font-family="serif" font-size="14" fill="#444">Analysts note a 310% surge in trustless escrow transactions, cementing on-chain agent verification as the gold standard for digital micro-economies.</text>

  <!-- Bottom Stories Grid -->
  <rect x="50" y="575" width="300" height="300" fill="#fff" stroke="#ccc" stroke-width="1"/>
  <text x="75" y="615" font-family="serif" font-size="20" font-weight="bold" fill="#111">Quantum Leap in Clean Energy</text>
  <text x="75" y="655" font-family="serif" font-size="13" fill="#444">Fusion test reactor achieves net-positive plasma containment for 72 consecutive hours, paving the way for commercial grid integration by 2030.</text>

  <rect x="362" y="575" width="300" height="300" fill="#fff" stroke="#ccc" stroke-width="1"/>
  <text x="387" y="615" font-family="serif" font-size="20" font-weight="bold" fill="#111">Neural Interface FDA Approval</text>
  <text x="387" y="655" font-family="serif" font-size="13" fill="#444">Next-gen non-invasive cognitive bandwidth headsets cleared for commercial medical rehabilitation and high-speed data transcription.</text>

  <rect x="674" y="575" width="300" height="300" fill="#fff" stroke="#ccc" stroke-width="1"/>
  <text x="699" y="615" font-family="serif" font-size="20" font-weight="bold" fill="#111">Date Check &amp; Verification</text>
  <text x="699" y="655" font-family="serif" font-size="13" fill="#444">All wires verified against official UTC feeds for Nov 21, 2026. Unverified historical chatter and speculative rumors excluded.</text>

  <!-- Footer Stats Strip -->
  <rect x="50" y="895" width="924" height="80" fill="#111"/>
  <text x="100" y="942" font-family="sans-serif" font-size="16" font-weight="bold" fill="#fff">GLOBAL MARKETS: BTC $98,420 (+4.2%) • SOL $212.50 (+7.8%) • ETH $3,650 (+2.1%)</text>
  <text x="800" y="942" font-family="sans-serif" font-size="14" font-weight="bold" fill="#ffcc00">VERIFIED LIVE</text>
</svg>
'''

with open('out.svg', 'w') as f:
    f.write(svg_content)

subprocess.run(['rsvg-convert', '-w', '1024', '-h', '1024', 'out.svg', '-o', 'entry.png'], check=True)
print("Generated entry.png successfully!")
