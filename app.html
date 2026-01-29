import React, { useState, useEffect } from 'react';
import { 
  BookOpen, 
  Users, 
  Heart, 
  Shield, 
  Activity, 
  CheckCircle, 
  ChevronRight, 
  ChevronLeft, 
  Menu,
  X,
  PieChart,
  Edit3,
  Award,
  AlertCircle,
  MessageCircle,
  Lock,
  Target,
  Eye,
  List,
  Scale,
  Lightbulb,
  Brain,
  CheckSquare,
  Zap,
  TrendingUp,
  CreditCard,
  Smile,
  AlertTriangle,
  Home,
  PlayCircle
} from 'lucide-react';

// --- Types & Interfaces ---

interface Section {
  id: string;
  title: string;
  icon: React.ReactNode;
  description: string;
  pages: Page[];
}

interface Page {
  id: string;
  title: string;
  type: 'content' | 'activity' | 'quiz' | 'diagram';
  content?: React.ReactNode;
  activityId?: string;
  quizId?: string;
}

interface QuizQuestion {
  question: string;
  options: string[];
  correctIndex: number;
}

interface SortItem {
  text: string;
  category: string;
  feedback: string;
}

// --- Data Content ---

const WILLNER_LIKED = [
  "Making requests instead of demands", "Calm, pleasant voice tone", 
  "Offering help", "Joking/Humor", "Positive feedback", "Fairness", 
  "Explaining 'Why' (Rationales)", "Enthusiasm", "Politeness", "Smiling"
];

const WILLNER_DISLIKED = [
  "Describing only wrongs", "Anger", "Negative feedback", "Profanity", 
  "Lack of understanding", "Bossy/Demanding", "Unpleasant physical contact", 
  "Mean/Insulting remarks", "Shouting", "Accusing/Blaming"
];

const BEHAVIOR_VS_LABEL: SortItem[] = [
  { text: "Hitting a peer", category: "behavior", feedback: "Yes! This is observable and measurable." },
  { text: "Aggressive", category: "label", feedback: "Correct. 'Aggressive' is a judgment/label, not a specific action." },
  { text: "Rolling eyes", category: "behavior", feedback: "Yes! You can see this happen." },
  { text: "Disrespectful", category: "label", feedback: "Correct. This is an interpretation, not a specific behavior." },
  { text: "Yelling 'No!'", category: "behavior", feedback: "Yes! This is specific verbal behavior." },
  { text: "Bad attitude", category: "label", feedback: "Correct. This is vague and judgmental." },
  { text: "Slouching in chair", category: "behavior", feedback: "Yes! This is observable body language." },
  { text: "Lazy", category: "label", feedback: "Correct. 'Lazy' is a label. The behavior might be 'sleeping late'." }
];

const PRINCIPLE_SCENARIOS = [
  {
    text: "Johnny is loud. You explain voice volume varies by situation (loud outside, soft inside). Johnny begins to use a lower voice inside.",
    principle: "Discrimination",
    feedback: "Correct! Discrimination is teaching that behavior appropriate in one situation may be inappropriate in another."
  },
  {
    text: "Michelle is shy. Her parents first reinforce eye contact, then a smile, and finally a handshake. Eventually, she greets visitors.",
    principle: "Shaping",
    feedback: "Correct! Shaping is reinforcing approximations (small steps) towards the final complex behavior."
  },
  {
    text: "Carlos gets a sticker for saying 'please'. Now his book is full and he doesn't want stickers anymore.",
    principle: "Satiation",
    feedback: "Correct! Satiation occurs when a reinforcer is used so much it loses its motivating power."
  }
];

const RATIONALE_SCENARIOS = [
  {
    situation: "Accepting Criticism",
    options: [
      "If you can accept criticism you'll learn to do things correctly and possibly avoid making the same mistake in the future.",
      "It's important to accept criticism because everyone has to hear feedback and it will help you to get a job."
    ],
    correctIndex: 0,
    explanation: "Option A is specific and provides a direct 'Benefit to Self' (avoiding mistakes)."
  },
  {
    situation: "Giving Criticism",
    options: [
      "If you give criticism in the right way, you can be sure that others will do things the way you want.",
      "When you give criticism in the right way, you give others a chance to learn without hurting their feelings."
    ],
    correctIndex: 1,
    explanation: "Option B is a 'Concern for Others' rationale that emphasizes positive relationships."
  }
];

const QUIZZES: Record<string, QuizQuestion[]> = {
  intro: [
    {
      question: "What is the end goal of all Boys Town treatment and services?",
      options: ["Temporary safety", "Permanency", "Strict discipline", "Isolation"],
      correctIndex: 1
    },
    {
      question: "Who are considered the primary change agents?",
      options: ["Doctors", "Judges", "People closest to the children (Staff/Family)", "Administrators"],
      correctIndex: 2
    }
  ],
  principles: [
    {
      question: "In the ABC pattern, what does 'A' stand for?",
      options: ["Action", "Antecedent", "Attitude", "Authority"],
      correctIndex: 1
    },
    {
      question: "Which consequence decreases behavior by taking away something positive?",
      options: ["Positive Reinforcement", "Negative Reinforcement", "Response Cost", "Natural Consequence"],
      correctIndex: 2
    }
  ],
  motivation: [
    {
      question: "What is the primary purpose of the Motivation System?",
      options: ["To punish youth", "To make staff's job easier", "To motivate youth to learn and change behavior", "To track attendance"],
      correctIndex: 2
    },
    {
      question: "Which level is for serious rule infractions like aggression or stealing?",
      options: ["Level I", "Level III", "ITL (Intensive Treatment Level)", "Level IV"],
      correctIndex: 2
    }
  ]
};

// --- Main Application Component ---

export default function App() {
  const [activeSection, setActiveSection] = useState<number>(-1); // -1 indicates HOME page
  const [activePage, setActivePage] = useState<number>(0);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  
  // State for interactive elements
  const [journalEntries, setJournalEntries] = useState<Record<string, string>>({});
  const [quizScores, setQuizScores] = useState<Record<string, boolean[]>>({});
  
  // Navigation Helper
  const navigateTo = (sectionIdx: number, pageIdx: number) => {
    setActiveSection(sectionIdx);
    setActivePage(pageIdx);
    setSidebarOpen(false); // Close sidebar on mobile selection
    window.scrollTo(0,0);
  };

  const handleNext = () => {
    if (activeSection === -1) return; // Should not happen

    const currentSectionData = SECTIONS[activeSection];
    if (activePage < currentSectionData.pages.length - 1) {
      setActivePage(activePage + 1);
    } else if (activeSection < SECTIONS.length - 1) {
      // Move to next section
      setActiveSection(activeSection + 1);
      setActivePage(0);
    } else {
      // Finished all sections, return home
      setActiveSection(-1);
    }
    window.scrollTo(0,0);
  };

  const handlePrev = () => {
    if (activeSection === -1) return;

    if (activePage > 0) {
      setActivePage(activePage - 1);
    } else if (activeSection > 0) {
      // Go to previous section's last page
      setActiveSection(activeSection - 1);
      setActivePage(SECTIONS[activeSection - 1].pages.length - 1);
    } else {
      // Back from first section -> Home
      setActiveSection(-1);
    }
    window.scrollTo(0,0);
  };

  // Content Structure - ORGANIZED BY TOC
  const SECTIONS: Section[] = [
    {
      id: 'intro',
      title: "Introduction to PEM",
      description: "Hallmarks, core principles, and the systems approach.",
      icon: <Shield className="w-5 h-5" />,
      pages: [
        { id: 'intro-welcome', title: 'Welcome & Hallmarks', type: 'content', content: <WelcomeContent /> },
        { id: 'intro-hallmarks', title: 'Core Principles', type: 'content', content: <HallmarksContent /> },
        { id: 'intro-pem', title: 'PEM Components', type: 'content', content: <PEMOverviewContent /> },
        { id: 'intro-systems', title: 'The Systems Approach', type: 'diagram', content: <PEMSystemsDiagram /> },
        { id: 'intro-bps', title: 'Bio-Psycho-Social Model', type: 'diagram', content: <BPSDiagram /> },
        { id: 'quiz-intro', title: 'Knowledge Check', type: 'quiz', quizId: 'intro' }
      ]
    },
    {
      id: 'pro-role',
      title: 'Professional Role',
      description: "Ethics, boundaries, and professional growth.",
      icon: <Award className="w-5 h-5" />,
      pages: [
        { id: 'pro-role-def', title: 'The Professional Role', type: 'content', content: <ProfessionalismContent /> },
        { id: 'pro-growth', title: 'Growth & Feedback', type: 'content', content: <ProfessionalGrowthContent /> },
        { id: 'pro-boundaries', title: 'Maintaining Boundaries', type: 'content', content: <BoundariesContent /> },
        { id: 'pro-plan', title: 'Personal Action Plan', type: 'activity', activityId: 'action-plan' }
      ]
    },
    {
      id: 'relationships',
      title: 'Therapeutic Relationships',
      description: "Building trust, the Willner study, and quality components.",
      icon: <Heart className="w-5 h-5" />,
      pages: [
        { id: 'rel-types', title: 'Defining Relationships', type: 'content', content: <RelationshipsContent /> },
        { id: 'rel-willner', title: 'The Willner Study', type: 'activity', activityId: 'willner-sort' },
        { id: 'rel-quality', title: 'Quality Components', type: 'diagram', content: <QualityComponentsDiagram /> },
        { id: 'rel-assess', title: 'Assessment', type: 'activity', activityId: 'assessment' }
      ]
    },
    {
      id: 'observing',
      title: 'Observing Behavior',
      description: "How to objectively observe and describe behaviors.",
      icon: <Eye className="w-5 h-5" />,
      pages: [
        { id: 'obs-def', title: 'What is Behavior?', type: 'content', content: <ObservingIntroContent /> },
        { id: 'obs-sort', title: 'Activity: Behavior vs. Label', type: 'activity', activityId: 'behavior-sort' }
      ]
    },
    {
      id: 'skills',
      title: 'Teaching Treatment Skills',
      description: "Social skills curriculum and target skills.",
      icon: <List className="w-5 h-5" />,
      pages: [
        { id: 'skills-intro', title: 'Teaching Skills', type: 'diagram', content: <SkillsDiagram /> },
        { id: 'skills-list', title: 'Curriculum Levels', type: 'content', content: <SkillsListContent /> },
        { id: 'skills-target', title: 'Target Skills', type: 'content', content: <TargetSkillsContent /> }
      ]
    },
    {
      id: 'tolerances',
      title: 'Tolerances',
      description: "Establishing consistent and reasonable tolerances.",
      icon: <Scale className="w-5 h-5" />,
      pages: [
        { id: 'tol-def', title: 'Understanding Tolerances', type: 'diagram', content: <TolerancesDiagram /> },
        { id: 'tol-types', title: 'Types of Tolerances', type: 'content', content: <ToleranceTypesContent /> }
      ]
    },
    {
      id: 'rationales',
      title: 'Rationales',
      description: "The 'Why' behind the behavior.",
      icon: <Lightbulb className="w-5 h-5" />,
      pages: [
        { id: 'rat-def', title: 'Using Rationales', type: 'content', content: <RationalesContent /> },
        { id: 'rat-quiz', title: 'Activity: Effective Rationales', type: 'activity', activityId: 'rationale-quiz' }
      ]
    },
    {
      id: 'principles',
      title: 'Principles of Behavior',
      description: "The ABC pattern and reinforcement strategies.",
      icon: <Brain className="w-5 h-5" />,
      pages: [
        { id: 'prin-abc', title: 'The ABC Pattern', type: 'diagram', content: <ABCDiagram /> },
        { id: 'prin-cons', title: 'Consequences', type: 'content', content: <ConsequencesContent /> },
        { id: 'prin-game', title: 'Game: Name That Principle', type: 'activity', activityId: 'principles-game' },
        { id: 'quiz-prin', title: 'Knowledge Check', type: 'quiz', quizId: 'principles' }
      ]
    },
    {
      id: 'motivation',
      title: 'Motivation System',
      description: "Point cards, levels, and privileges.",
      icon: <Zap className="w-5 h-5" />,
      pages: [
        { id: 'mot-overview', title: 'System Overview', type: 'content', content: <MotivationOverviewContent /> },
        { id: 'mot-card', title: 'Point Card Mechanics', type: 'diagram', content: <PointCardDiagram /> },
        { id: 'mot-levels', title: 'Levels & Privileges', type: 'content', content: <LevelsContent /> },
        { id: 'quiz-mot', title: 'Knowledge Check', type: 'quiz', quizId: 'motivation' }
      ]
    },
    {
      id: 'teaching-strat',
      title: 'Teaching Strategies',
      description: "Proactive teaching, effective praise, and corrective teaching.",
      icon: <Target className="w-5 h-5" />,
      pages: [
        { id: 'teach-pro', title: 'Proactive Teaching', type: 'content', content: <ProactiveTeachingContent /> },
        { id: 'teach-praise', title: 'Effective Praise', type: 'content', content: <EffectivePraiseContent /> },
        { id: 'teach-correct', title: 'Corrective Teaching', type: 'content', content: <CorrectiveTeachingContent /> }
      ]
    }
  ];

  const CurrentPage = activeSection >= 0 ? SECTIONS[activeSection].pages[activePage] : null;

  return (
    <div className="flex h-screen bg-slate-50 text-slate-800 font-sans overflow-hidden">
      
      {/* Mobile Sidebar Overlay */}
      {sidebarOpen && (
        <div 
          className="fixed inset-0 bg-slate-900/50 z-40 md:hidden backdrop-blur-sm"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* Sidebar Navigation */}
      <div className={`fixed inset-y-0 left-0 z-50 w-72 bg-slate-900 text-white transform transition-transform duration-300 ease-in-out ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'} md:relative md:translate-x-0 flex flex-col shadow-xl`}>
        <div className="p-6 border-b border-slate-700 flex justify-between items-center">
          <div className="flex items-center cursor-pointer" onClick={() => navigateTo(-1, 0)}>
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center mr-3 font-bold text-white">BT</div>
            <div>
              <h1 className="text-lg font-bold text-white">Boys Town</h1>
              <p className="text-xs text-slate-400">PEM Tool</p>
            </div>
          </div>
          <button onClick={() => setSidebarOpen(false)} className="md:hidden text-slate-400 hover:text-white p-2">
            <X size={24} />
          </button>
        </div>
        
        <nav className="flex-1 overflow-y-auto py-4">
          {/* Home Button */}
          <button 
            onClick={() => navigateTo(-1, 0)}
            className={`w-full flex items-center px-6 py-3 text-left transition-colors mb-2 ${activeSection === -1 ? 'bg-blue-700 text-white border-l-4 border-blue-400' : 'text-slate-300 hover:bg-slate-800'}`}
          >
            <Home className="w-5 h-5 mr-3" />
            <span className="font-medium text-sm">Dashboard</span>
          </button>

          <div className="px-6 py-2 text-xs font-bold text-slate-500 uppercase tracking-wider">Modules</div>

          {SECTIONS.map((section, sIdx) => (
            <div key={section.id} className="mb-1">
              <button 
                onClick={() => navigateTo(sIdx, 0)}
                className={`w-full flex items-center px-6 py-2.5 text-left transition-colors ${activeSection === sIdx ? 'bg-slate-800 text-white border-l-4 border-blue-500' : 'text-slate-300 hover:bg-slate-800'}`}
              >
                <span className={`mr-3 ${activeSection === sIdx ? 'text-blue-400' : 'text-slate-500'}`}>{section.icon}</span>
                <span className="font-medium text-sm truncate">{section.title}</span>
              </button>
              
              {activeSection === sIdx && (
                <div className="bg-slate-950/30 py-1">
                  {section.pages.map((page, pIdx) => (
                    <button
                      key={page.id}
                      onClick={() => navigateTo(sIdx, pIdx)}
                      className={`w-full flex items-center pl-14 pr-6 py-2 text-xs text-left ${activePage === pIdx ? 'text-blue-400 font-semibold' : 'text-slate-500 hover:text-slate-300'}`}
                    >
                      {activePage === pIdx && <div className="w-1.5 h-1.5 rounded-full bg-blue-400 mr-2" />}
                      {page.title}
                    </button>
                  ))}
                </div>
              )}
            </div>
          ))}
        </nav>
        
        <div className="p-4 border-t border-slate-700">
          <div className="text-xs text-slate-500 text-center">
            Structure: Official TOC<br/>Complete Curriculum
          </div>
        </div>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col h-full overflow-hidden w-full relative">
        {/* Mobile Header */}
        <header className="bg-white border-b border-slate-200 p-4 flex items-center justify-between md:hidden sticky top-0 z-30 shadow-sm">
          <div className="flex items-center">
            <button onClick={() => setSidebarOpen(true)} className="text-slate-600 mr-3 p-1 hover:bg-slate-100 rounded">
              <Menu size={24} />
            </button>
            <h2 className="font-semibold text-slate-800 truncate text-sm max-w-[200px]">
              {activeSection === -1 ? "Dashboard" : SECTIONS[activeSection].title}
            </h2>
          </div>
          {activeSection !== -1 && (
            <div className="text-xs text-slate-400 font-mono">
              {activePage + 1}/{SECTIONS[activeSection].pages.length}
            </div>
          )}
        </header>

        {/* Scrollable Content */}
        <main className="flex-1 overflow-y-auto bg-slate-50">
          
          {activeSection === -1 ? (
            /* --- HOME DASHBOARD --- */
            <div className="p-4 md:p-8 max-w-7xl mx-auto">
              <div className="mb-8">
                <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-2">Welcome Back</h1>
                <p className="text-slate-600">Select a module to begin your training on the Boys Town Teaching Model.</p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {SECTIONS.map((section, idx) => (
                  <button 
                    key={section.id}
                    onClick={() => navigateTo(idx, 0)}
                    className="flex flex-col bg-white border border-slate-200 rounded-xl p-6 shadow-sm hover:shadow-md hover:border-blue-300 transition-all text-left group h-full"
                  >
                    <div className="flex items-start justify-between mb-4 w-full">
                      <div className="p-3 bg-blue-50 text-blue-600 rounded-lg group-hover:bg-blue-600 group-hover:text-white transition-colors">
                        {section.icon}
                      </div>
                      <span className="text-xs font-semibold bg-slate-100 text-slate-500 px-2 py-1 rounded">
                        {section.pages.length} Pages
                      </span>
                    </div>
                    <h3 className="text-lg font-bold text-slate-800 mb-2 group-hover:text-blue-700">{section.title}</h3>
                    <p className="text-sm text-slate-500 mb-4 flex-grow">{section.description}</p>
                    <div className="flex items-center text-blue-600 text-sm font-semibold mt-auto">
                      Start Module <ChevronRight size={16} className="ml-1" />
                    </div>
                  </button>
                ))}
              </div>
            </div>
          ) : (
            /* --- MODULE CONTENT --- */
            <div className="p-4 md:p-8 lg:p-12 min-h-full">
              <div className="max-w-4xl mx-auto bg-white rounded-xl shadow-sm border border-slate-100 min-h-[calc(100vh-140px)] flex flex-col">
                
                {/* Page Header */}
                <div className="p-4 md:p-8 border-b border-slate-100">
                   <div className="flex items-center text-xs md:text-sm text-blue-600 font-medium mb-2 uppercase tracking-wide">
                     <span className="truncate cursor-pointer hover:underline" onClick={() => navigateTo(-1, 0)}>Dashboard</span> 
                     <ChevronRight size={14} className="mx-1 flex-shrink-0"/> 
                     <span className="truncate">{SECTIONS[activeSection].title}</span> 
                     <ChevronRight size={14} className="mx-1 flex-shrink-0"/> 
                     <span className="truncate text-slate-400">{CurrentPage?.title}</span>
                   </div>
                   <h1 className="text-2xl md:text-3xl font-bold text-slate-900 leading-tight">{CurrentPage?.title}</h1>
                </div>

                {/* Dynamic Content Rendering */}
                <div className="p-4 md:p-8 flex-1">
                  {CurrentPage?.type === 'content' && CurrentPage.content}
                  {CurrentPage?.type === 'diagram' && CurrentPage.content}
                  {CurrentPage?.type === 'quiz' && CurrentPage.quizId && (
                    <QuizComponent 
                      id={CurrentPage.quizId} 
                      data={QUIZZES[CurrentPage.quizId]} 
                      scores={quizScores}
                      setScores={setQuizScores}
                    />
                  )}
                  {CurrentPage?.type === 'activity' && CurrentPage.activityId === 'willner-sort' && (
                    <WillnerSortGame />
                  )}
                  {CurrentPage?.type === 'activity' && CurrentPage.activityId === 'behavior-sort' && (
                    <BehaviorSortGame />
                  )}
                  {CurrentPage?.type === 'activity' && CurrentPage.activityId === 'rationale-quiz' && (
                    <RationaleQuiz />
                  )}
                  {CurrentPage?.type === 'activity' && CurrentPage.activityId === 'principles-game' && (
                    <PrinciplesGame />
                  )}
                  {CurrentPage?.type === 'activity' && CurrentPage.activityId === 'action-plan' && (
                    <JournalActivity 
                      id="action_plan"
                      prompt="What are one or two of the most important things you learned in this section? What do you plan to do differently?"
                      entries={journalEntries}
                      setEntries={setJournalEntries}
                    />
                  )}
                  {CurrentPage?.type === 'activity' && CurrentPage.activityId === 'assessment' && (
                    <JournalActivity 
                      id="rel_assessment"
                      prompt="Reflect: Do the youth you work with seem to want to be around you? How are your Quality Components (voice tone, proximity) when interacting?"
                      entries={journalEntries}
                      setEntries={setJournalEntries}
                    />
                  )}
                </div>

                {/* Footer Navigation */}
                <div className="p-4 md:p-6 bg-slate-50 border-t border-slate-100 flex justify-between items-center rounded-b-xl sticky bottom-0 z-20">
                  <button 
                    onClick={handlePrev}
                    className="flex items-center px-3 py-2 md:px-4 rounded-lg text-sm font-medium transition-colors text-slate-600 hover:bg-slate-200"
                  >
                    <ChevronLeft size={16} className="mr-1 md:mr-2" /> 
                    <span className="hidden xs:inline">{activePage === 0 && activeSection === 0 ? "Back to Home" : "Previous"}</span>
                    <span className="xs:hidden">Back</span>
                  </button>
                  
                  <div className="text-xs text-slate-400 font-mono hidden sm:block">
                    Page {activePage + 1} of {SECTIONS[activeSection].pages.length}
                  </div>

                  <button 
                    onClick={handleNext}
                    className={`flex items-center px-4 py-2 md:px-6 rounded-lg text-sm font-medium transition-colors ${activeSection === SECTIONS.length - 1 && activePage === SECTIONS[activeSection].pages.length - 1 ? 'bg-slate-800 text-white' : 'bg-blue-600 text-white hover:bg-blue-700 shadow-sm'}`}
                  >
                    {activeSection === SECTIONS.length - 1 && activePage === SECTIONS[activeSection].pages.length - 1 ? 'Finish' : 'Next'} <ChevronRight size={16} className="ml-1 md:ml-2" />
                  </button>
                </div>

              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}

// --- NEW TEACHING INTERACTION SECTIONS (Placeholders/Summaries) ---

function ProactiveTeachingContent() {
  return (
    <div className="space-y-6">
      <div className="bg-green-50 p-6 rounded-lg border-l-4 border-green-500">
        <h3 className="text-xl font-bold text-green-900 mb-2 flex items-center"><Target className="mr-2"/> Proactive Teaching</h3>
        <p className="text-green-800">Setting youth up for success before behavior occurs.</p>
      </div>
      <div className="grid gap-4">
        <div className="bg-white p-4 rounded shadow-sm border">
          <strong className="block text-slate-800 mb-2">When to use:</strong>
          <p className="text-sm text-slate-600">Before a situation where a youth might struggle (e.g., before going into a store, before a family visit).</p>
        </div>
        <div className="bg-white p-4 rounded shadow-sm border">
          <strong className="block text-slate-800 mb-2">Key Steps:</strong>
          <ul className="list-disc list-inside text-sm text-slate-600 space-y-1">
            <li>Communicate clear expectations.</li>
            <li>Rehearse the desired behavior.</li>
            <li>Establish motivation (Rationales).</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

function EffectivePraiseContent() {
  return (
    <div className="space-y-6">
      <div className="bg-blue-50 p-6 rounded-lg border-l-4 border-blue-500">
        <h3 className="text-xl font-bold text-blue-900 mb-2 flex items-center"><Smile className="mr-2"/> Effective Praise</h3>
        <p className="text-blue-800">Focusing on positive behavior to reinforce it.</p>
      </div>
      <p className="text-slate-600">
        Effective praise goes beyond "Good job." It is specific and sincere.
      </p>
      <div className="bg-white p-4 rounded shadow-sm border">
        <strong className="block text-slate-800 mb-2">Components:</strong>
        <ul className="list-disc list-inside text-sm text-slate-600 space-y-2">
          <li><strong>Show Approval:</strong> Smile, nod, "Great work!"</li>
          <li><strong>Describe Behavior:</strong> "You followed instructions by turning off the TV immediately."</li>
          <li><strong>Give Rationale:</strong> "This shows you are responsible."</li>
          <li><strong>Positive Consequence:</strong> Give points or privileges.</li>
        </ul>
      </div>
    </div>
  );
}

function CorrectiveTeachingContent() {
  return (
    <div className="space-y-6">
      <div className="bg-orange-50 p-6 rounded-lg border-l-4 border-orange-500">
        <h3 className="text-xl font-bold text-orange-900 mb-2 flex items-center"><AlertTriangle className="mr-2"/> Corrective Teaching</h3>
        <p className="text-orange-800">Teaching an alternative to inappropriate behavior.</p>
      </div>
      <div className="space-y-4">
        <p className="text-slate-700 font-medium">The goal is to stop the behavior and teach a better way.</p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 border rounded">
            <div className="font-bold text-slate-700">1. Initial Praise/Empathy</div>
            <div className="text-xs text-slate-500">"I know you're frustrated..."</div>
          </div>
          <div className="bg-white p-4 border rounded">
            <div className="font-bold text-slate-700">2. Describe Inappropriate Behavior</div>
            <div className="text-xs text-slate-500">"But you yelled and threw the book."</div>
          </div>
          <div className="bg-white p-4 border rounded">
            <div className="font-bold text-slate-700">3. Give Consequence</div>
            <div className="text-xs text-slate-500">Negative points (Response Cost).</div>
          </div>
          <div className="bg-white p-4 border rounded">
            <div className="font-bold text-slate-700">4. Describe Appropriate Behavior</div>
            <div className="text-xs text-slate-500">"Next time, ask for a break."</div>
          </div>
          <div className="bg-white p-4 border rounded">
            <div className="font-bold text-slate-700">5. Practice</div>
            <div className="text-xs text-slate-500">"Let's try asking for a break now."</div>
          </div>
        </div>
      </div>
    </div>
  );
}

// --- EXISTING COMPONENTS (Unchanged logic, just mapping) ---

function ABCDiagram() {
  return (
    <div className="flex flex-col items-center space-y-8">
      <div className="bg-blue-50 p-4 rounded-lg border border-blue-200 w-full">
        <h4 className="font-bold text-blue-900 mb-2">The ABC Pattern</h4>
        <p className="text-sm text-blue-800">Behavior doesn't happen in a vacuum. Understanding what comes before and after is key to treatment.</p>
      </div>

      <div className="flex flex-col md:flex-row items-stretch justify-center gap-4 w-full">
        {/* Antecedent */}
        <div className="flex-1 bg-white border-2 border-indigo-200 rounded-xl p-6 flex flex-col items-center text-center shadow-sm">
          <div className="w-12 h-12 bg-indigo-100 text-indigo-600 rounded-full flex items-center justify-center font-bold text-xl mb-4">A</div>
          <h5 className="font-bold text-slate-800 mb-2">Antecedent</h5>
          <p className="text-xs text-slate-500">Events or conditions present <strong>before</strong> a behavior occurs. (Who, when, where).</p>
        </div>

        <div className="hidden md:flex items-center text-slate-300">
          <ChevronRight size={32} />
        </div>
        <div className="md:hidden flex justify-center text-slate-300 transform rotate-90">
          <ChevronRight size={24} />
        </div>

        {/* Behavior */}
        <div className="flex-1 bg-white border-2 border-green-200 rounded-xl p-6 flex flex-col items-center text-center shadow-sm">
          <div className="w-12 h-12 bg-green-100 text-green-600 rounded-full flex items-center justify-center font-bold text-xl mb-4">B</div>
          <h5 className="font-bold text-slate-800 mb-2">Behavior</h5>
          <p className="text-xs text-slate-500">Anything a person says or does that can be <strong>observed and measured</strong>.</p>
        </div>

        <div className="hidden md:flex items-center text-slate-300">
          <ChevronRight size={32} />
        </div>
        <div className="md:hidden flex justify-center text-slate-300 transform rotate-90">
          <ChevronRight size={24} />
        </div>

        {/* Consequence */}
        <div className="flex-1 bg-white border-2 border-orange-200 rounded-xl p-6 flex flex-col items-center text-center shadow-sm">
          <div className="w-12 h-12 bg-orange-100 text-orange-600 rounded-full flex items-center justify-center font-bold text-xl mb-4">C</div>
          <h5 className="font-bold text-slate-800 mb-2">Consequence</h5>
          <p className="text-xs text-slate-500">Events that occur <strong>after</strong> a behavior. Determines if behavior happens again.</p>
        </div>
      </div>
    </div>
  );
}

function ConsequencesContent() {
  return (
    <div className="space-y-8">
      <div>
        <h3 className="text-lg font-bold text-slate-800 mb-4">Types of Reinforcement</h3>
        <div className="grid grid-cols-1 gap-4">
          <div className="bg-green-50 p-4 rounded-lg border-l-4 border-green-500">
            <div className="flex justify-between items-start">
              <div>
                <strong className="text-green-900 block">Positive Reinforcement</strong>
                <span className="text-xs text-green-800">Something <strong>good</strong> happens. Behavior increases.</span>
              </div>
              <TrendingUp className="text-green-600" />
            </div>
          </div>
          <div className="bg-blue-50 p-4 rounded-lg border-l-4 border-blue-500">
            <div className="flex justify-between items-start">
              <div>
                <strong className="text-blue-900 block">Negative Reinforcement</strong>
                <span className="text-xs text-blue-800">Something <strong>unpleasant is removed</strong>. Behavior increases.</span>
              </div>
              <TrendingUp className="text-blue-600" />
            </div>
          </div>
          <div className="bg-orange-50 p-4 rounded-lg border-l-4 border-orange-500">
            <div className="flex justify-between items-start">
              <div>
                <strong className="text-orange-900 block">Response Cost</strong>
                <span className="text-xs text-orange-800">Taking away something positive (e.g., points). Behavior decreases.</span>
              </div>
              <div className="transform rotate-180"><TrendingUp className="text-orange-600" /></div>
            </div>
          </div>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-bold text-slate-800 mb-4">Characteristics of Effective Consequences</h3>
        <ul className="space-y-2 text-sm text-slate-600">
          <li className="flex items-center"><CheckSquare size={16} className="text-slate-400 mr-2"/> <strong>Individualized:</strong> Specific to what the youth likes/dislikes.</li>
          <li className="flex items-center"><CheckSquare size={16} className="text-slate-400 mr-2"/> <strong>Proportional:</strong> The size fits the behavior.</li>
          <li className="flex items-center"><CheckSquare size={16} className="text-slate-400 mr-2"/> <strong>Immediate:</strong> Delivered right after behavior.</li>
          <li className="flex items-center"><CheckSquare size={16} className="text-slate-400 mr-2"/> <strong>Contingent:</strong> Only after behavior is displayed.</li>
        </ul>
      </div>
    </div>
  );
}

function MotivationOverviewContent() {
  return (
    <div className="space-y-6">
      <p className="text-slate-700">
        The PEM Motivation System is a behavior management system designed to provide a systematic, positive approach. It couples motivation with teaching.
      </p>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-white border rounded-lg p-4 shadow-sm">
          <h4 className="font-bold text-slate-800 mb-2">Hallmarks of the System</h4>
          <ul className="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li>Utilizes principles of behavior</li>
            <li>Coupled with teaching (not just points)</li>
            <li>Focuses on the positive (8:1 ratio)</li>
            <li>Structured & Consistent</li>
            <li>Provides documentation</li>
          </ul>
        </div>
        <div className="bg-white border rounded-lg p-4 shadow-sm">
          <h4 className="font-bold text-slate-800 mb-2">Artificial Consequences</h4>
          <p className="text-xs text-slate-600 mb-2">
            Points are "Artificial Consequences". Like a paycheck, they are not reinforcing by themselves, but by what they can purchase (Privileges).
          </p>
          <div className="flex items-center text-xs font-bold text-slate-500">
            <CreditCard size={16} className="mr-2"/> Points = Access to Privileges
          </div>
        </div>
      </div>
    </div>
  );
}

function PointCardDiagram() {
  return (
    <div className="flex flex-col items-center">
      <h3 className="text-lg font-bold mb-4">Point Card Mechanics</h3>
      <div className="w-full max-w-md bg-white border-2 border-slate-300 rounded-lg p-4 shadow-md text-sm">
        <div className="flex justify-between border-b pb-2 mb-2 font-bold text-slate-700">
          <span>Target Skill (+100)</span>
          <span>Target Skill (-200)</span>
        </div>
        <div className="flex justify-between font-medium text-slate-500">
          <span>Non-Target Skill (+50)</span>
          <span>Non-Target Skill (-100)</span>
        </div>
        
        <div className="mt-6 bg-slate-50 p-3 rounded text-xs text-slate-600">
          <strong>Key Rule:</strong> Write skills in the <em>positive</em> (e.g., "Following Instructions" not "Refusing").
        </div>
      </div>
      <p className="mt-4 text-xs text-slate-500 text-center">
        Positive points are earned for Proactive Teaching and Effective Praise.<br/>
        Negative points (Response Cost) are for Corrective Teaching.
      </p>
    </div>
  );
}

function LevelsContent() {
  return (
    <div className="space-y-6">
      <div className="overflow-x-auto pb-2">
        <table className="w-full text-sm min-w-[500px] border-collapse">
          <thead>
            <tr className="bg-slate-100 text-slate-700 text-left">
              <th className="p-3 rounded-tl-lg">Level</th>
              <th className="p-3">Focus</th>
              <th className="p-3 rounded-tr-lg">Advancement Criteria</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-slate-100">
              <td className="p-3 font-bold text-blue-600">Level I</td>
              <td className="p-3 text-slate-600">Continuous reinforcement. High teaching (70-55/day).</td>
              <td className="p-3 text-slate-500">Start here.</td>
            </tr>
            <tr className="border-b border-slate-100">
              <td className="p-3 font-bold text-indigo-600">Level II</td>
              <td className="p-3 text-slate-600">Progress to independence. 50-45 interactions.</td>
              <td className="p-3 text-slate-500">21 days on Level I. 50k points.</td>
            </tr>
            <tr className="border-b border-slate-100">
              <td className="p-3 font-bold text-purple-600">Level III</td>
              <td className="p-3 text-slate-600">Positive Role Model. Social reinforcement.</td>
              <td className="p-3 text-slate-500">14 days on Level II. 75k points.</td>
            </tr>
            <tr>
              <td className="p-3 font-bold text-red-600">ITL</td>
              <td className="p-3 text-slate-600">Intensive Treatment. For major rule infractions.</td>
              <td className="p-3 text-slate-500">Earn off points to return to level.</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div className="bg-slate-50 p-4 rounded-lg">
        <h4 className="font-bold text-slate-800 mb-2">Privileges</h4>
        <p className="text-xs text-slate-600 mb-2">Points buy privileges. Privileges must be meaningful.</p>
        <div className="flex flex-wrap gap-2">
           <span className="bg-white border px-2 py-1 rounded text-xs">TV/Music</span>
           <span className="bg-white border px-2 py-1 rounded text-xs">Snacks</span>
           <span className="bg-white border px-2 py-1 rounded text-xs">Outings</span>
           <span className="bg-white border px-2 py-1 rounded text-xs">Later Bedtime</span>
        </div>
      </div>
    </div>
  );
}

function PrinciplesGame() {
  const [idx, setIdx] = useState(0);
  const [showResult, setShowResult] = useState(false);

  const handleNext = () => {
    setShowResult(false);
    setIdx((prev) => (prev + 1) % PRINCIPLE_SCENARIOS.length);
  };

  const current = PRINCIPLE_SCENARIOS[idx];

  return (
    <div className="bg-white border rounded-xl p-6 shadow-sm text-center">
      <h3 className="font-bold text-slate-800 mb-4">Name That Principle</h3>
      <p className="text-sm text-slate-600 mb-6 min-h-[60px]">{current.text}</p>
      
      {!showResult ? (
        <button 
          onClick={() => setShowResult(true)}
          className="bg-blue-600 text-white px-6 py-2 rounded-lg font-bold"
        >
          Reveal Principle
        </button>
      ) : (
        <div className="animate-in fade-in zoom-in duration-300">
          <div className="text-xl font-bold text-blue-600 mb-2">{current.principle}</div>
          <p className="text-xs text-slate-500 mb-4">{current.feedback}</p>
          <button 
            onClick={handleNext}
            className="text-blue-500 font-bold hover:underline"
          >
            Next Scenario &rarr;
          </button>
        </div>
      )}
    </div>
  );
}

// --- Content Components from Previous Turns (Optimized for Mobile) ---

function ObservingIntroContent() {
  return (
    <div className="space-y-6">
      <div className="bg-indigo-50 p-4 md:p-6 rounded-lg border border-indigo-100">
        <h3 className="text-lg font-bold text-indigo-900 mb-2">Definition of Behavior</h3>
        <p className="text-indigo-800 text-sm md:text-base">
          "Anything a person says or does that can be <strong>seen, heard, or measured</strong>."
        </p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <h4 className="font-bold text-slate-800 mb-2 flex items-center"><CheckCircle size={16} className="text-green-500 mr-2" /> Key Elements</h4>
          <ul className="text-sm text-slate-600 space-y-2 list-disc list-inside">
            <li><strong>Be Specific:</strong> Mirror behavior clearly.</li>
            <li><strong>Be Behavioral:</strong> Describe actions, not feelings.</li>
            <li><strong>Remain Objective:</strong> Avoid judgment.</li>
          </ul>
        </div>
        <div>
           <h4 className="font-bold text-slate-800 mb-2 flex items-center"><X size={16} className="text-red-500 mr-2" /> What is NOT Behavior?</h4>
           <ul className="text-sm text-slate-600 space-y-2 list-disc list-inside">
             <li><strong>Diagnoses:</strong> (e.g., ADHD, Depression)</li>
             <li><strong>Feelings:</strong> (e.g., Angry, Happy)</li>
             <li><strong>Labels:</strong> (e.g., Lazy, Rude, Crabby)</li>
           </ul>
        </div>
      </div>
    </div>
  );
}

function SkillsDiagram() {
  return (
    <div className="flex flex-col items-center py-8">
      <h3 className="text-xl font-bold mb-4">Teaching Skills</h3>
      <div className="relative w-[280px] h-[280px] sm:w-[300px] sm:h-[300px]">
        {/* Top Circle */}
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 w-32 h-32 sm:w-40 sm:h-40 rounded-full border-4 border-blue-400 bg-blue-50/50 flex items-center justify-center pt-8">
          <span className="font-bold text-blue-900 text-sm sm:text-base">Social</span>
        </div>
        {/* Left Circle */}
        <div className="absolute bottom-0 left-0 w-32 h-32 sm:w-40 sm:h-40 rounded-full border-4 border-green-400 bg-green-50/50 flex items-center justify-center pr-4 pb-4">
          <span className="font-bold text-green-900 text-sm sm:text-base">Academic</span>
        </div>
        {/* Right Circle */}
        <div className="absolute bottom-0 right-0 w-32 h-32 sm:w-40 sm:h-40 rounded-full border-4 border-orange-400 bg-orange-50/50 flex items-center justify-center pl-4 pb-4 text-center">
          <span className="font-bold text-orange-900 text-sm sm:text-base">Indep.<br/>Living</span>
        </div>
      </div>
    </div>
  );
}

function SkillsListContent() {
  return (
    <div className="space-y-6">
      <div className="bg-slate-50 p-4 rounded border">
        <h4 className="font-bold text-slate-800 mb-2">Definition of Social Skill</h4>
        <p className="text-sm text-slate-600">
          A series of related behaviors that constitute socially acceptable ways of behaving.
        </p>
      </div>
      <div className="space-y-4">
        <h3 className="font-bold text-lg">Curriculum Groups</h3>
        <div className="grid grid-cols-1 gap-4">
          <div className="border-l-4 border-green-500 pl-4 py-2">
            <div className="font-bold text-green-700">Group 1: Basic Skills</div>
            <div className="text-xs text-slate-500 mt-1">Following Instructions, Accepting "No", Introducing Yourself.</div>
          </div>
          <div className="border-l-4 border-blue-500 pl-4 py-2">
            <div className="font-bold text-blue-700">Group 2: Intermediate Skills</div>
            <div className="text-xs text-slate-500 mt-1">Apologizing, Asking for Help, Disagreeing Appropriately.</div>
          </div>
        </div>
      </div>
    </div>
  );
}

function TargetSkillsContent() {
  return (
    <div className="space-y-6">
       <h3 className="text-xl font-bold text-slate-800">Identifying Target Skills</h3>
       <p className="text-slate-600">
         Target skills are "Replacement Behaviors" for problem behaviors.
       </p>
       <div className="bg-white border rounded-xl p-4 md:p-6 shadow-sm">
         <h4 className="font-bold mb-4 flex items-center"><Target size={20} className="mr-2 text-red-500"/> The Process</h4>
         <div className="space-y-4">
           {[
             "Gather Information (Parents, Schools)",
             "Identify Problem Behaviors",
             "Match with Treatment Skills (PEM Curriculum)",
             "Teach! (All staff teach Target Skills)"
           ].map((step, i) => (
             <div key={i} className="flex items-start">
               <div className="bg-slate-200 rounded-full w-6 h-6 flex-shrink-0 flex items-center justify-center font-bold text-xs mr-3 mt-1">{i + 1}</div>
               <span className="text-sm text-slate-700">{step}</span>
             </div>
           ))}
         </div>
       </div>
    </div>
  );
}

function TolerancesDiagram() {
  return (
    <div className="space-y-8 flex flex-col items-center">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">
        <div className="border-2 border-slate-300 rounded h-32 relative bg-white flex flex-col justify-between p-2">
          <div className="w-full text-center text-xs font-bold text-red-500 border-b-4 border-red-500 pb-1">Unacceptable</div>
          <div className="text-center font-bold text-slate-400">High Tolerance</div>
          <div className="text-xs text-center text-slate-500">Lots of bad behavior accepted.</div>
        </div>
        <div className="border-2 border-slate-300 rounded h-32 relative bg-white flex flex-col justify-between p-2">
          <div className="text-center font-bold text-slate-400 pt-4">Low Tolerance</div>
          <div className="w-full text-center text-xs font-bold text-green-600 border-t-4 border-red-500 pt-1">Acceptable</div>
          <div className="text-xs text-center text-slate-500">Almost nothing accepted. Frustrating.</div>
        </div>
        <div className="border-2 border-slate-300 rounded h-32 relative bg-white ring-2 ring-blue-500 flex flex-col justify-between p-2">
           <div className="w-full text-center font-bold text-red-500">Unacceptable</div>
           <div className="w-full h-1 bg-red-500 my-auto relative">
             <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white px-2 text-xs font-bold text-slate-800 border border-slate-200 rounded">Reasonable</div>
           </div>
           <div className="w-full text-center font-bold text-green-600">Acceptable</div>
        </div>
      </div>
    </div>
  );
}

function ToleranceTypesContent() {
  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 gap-4">
        <div className="bg-white p-4 rounded shadow-sm border-l-4 border-indigo-500">
          <strong className="block text-indigo-700 mb-1">Personal Tolerance</strong>
          <span className="text-sm text-slate-600">What one individual staff member deems appropriate. Varies by person.</span>
        </div>
        <div className="bg-white p-4 rounded shadow-sm border-l-4 border-blue-500">
          <strong className="block text-blue-700 mb-1">Program Tolerance</strong>
          <span className="text-sm text-slate-600">The Goal. Consistent response across all staff.</span>
        </div>
        <div className="bg-white p-4 rounded shadow-sm border-l-4 border-green-500">
          <strong className="block text-green-700 mb-1">Youth Treatment Tolerance</strong>
          <span className="text-sm text-slate-600">Adjusting for individual youth based on age, culture, and treatment plans.</span>
        </div>
      </div>
    </div>
  );
}

function RationalesContent() {
  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-white p-4 border rounded-lg shadow-sm">
          <strong className="block text-slate-800 mb-2">Benefit to Self</strong>
          <p className="text-xs text-slate-500">"If you accept criticism, you will get better at what you do."</p>
        </div>
        <div className="bg-white p-4 border rounded-lg shadow-sm">
          <strong className="block text-slate-800 mb-2">Concern for Others</strong>
          <p className="text-xs text-slate-500">"If you speak softly, you won't bother others."</p>
        </div>
        <div className="bg-white p-4 border rounded-lg shadow-sm">
          <strong className="block text-slate-800 mb-2">Negative Outcome</strong>
          <p className="text-xs text-slate-500">"If you fight, you might get hurt." (Use sparingly).</p>
        </div>
      </div>
    </div>
  );
}

function WelcomeContent() {
  return (
    <div className="space-y-6">
      <div className="bg-blue-50 p-6 rounded-lg border border-blue-100">
        <h3 className="text-lg font-semibold text-blue-900 mb-2">About this Training</h3>
        <p className="text-blue-800 leading-relaxed text-sm md:text-base">
          This module covers the core philosophies of the Boys Town Model: Hallmarks, PEM, Behavior Principles, and Motivation Systems.
        </p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
        {["Safety", "Permanency", "Well-being", "Engagement"].map((h) => (
          <div key={h} className="p-4 border border-slate-200 rounded-lg hover:shadow-md transition-shadow">
            <div className="font-bold text-slate-700">{h}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function HallmarksContent() {
  return (
    <div className="space-y-8">
      <ul className="space-y-4 list-none pl-0">
        <li className="flex items-start">
          <CheckCircle className="w-6 h-6 text-green-500 mr-3 flex-shrink-0 mt-1" />
          <div>
            <strong className="block text-slate-900">People Closest are Change Agents</strong>
            <span className="text-sm text-slate-600">Those who spend the most time with children have the greatest impact.</span>
          </div>
        </li>
        <li className="flex items-start">
          <CheckCircle className="w-6 h-6 text-green-500 mr-3 flex-shrink-0 mt-1" />
          <div>
            <strong className="block text-slate-900">Behavioral Orientation</strong>
            <span className="text-sm text-slate-600">Documented effectiveness allowing for measurable change.</span>
          </div>
        </li>
      </ul>
    </div>
  );
}

function PEMOverviewContent() {
  return (
    <div className="space-y-6">
      <p className="text-lg text-slate-700">
        The Hallmarks form the basis of the <strong>Psychoeducational Treatment Model (PEM)®</strong>.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Building Relationships" icon={<Users className="text-blue-500"/>}>
          Staff build therapeutic, goal-oriented relationships and collaborate with youth to achieve goals.
        </Card>
        <Card title="Teaching Skills" icon={<BookOpen className="text-blue-500"/>}>
          A structured approach (teaching interactions) to teach social skills and self-control strategies.
        </Card>
        <Card title="Motivation System" icon={<Activity className="text-blue-500"/>}>
          Structured systems based on behavioral principles to motivate youth to change behavior.
        </Card>
        <Card title="Therapeutic Environment" icon={<Heart className="text-blue-500"/>}>
          A healthy environment including positive peer culture, family-style living, and self-government.
        </Card>
      </div>
    </div>
  );
}

function PEMSystemsDiagram() {
  return (
    <div className="flex flex-col items-center justify-center py-8">
      <h3 className="text-xl font-bold mb-8 text-center">PEM Systems Approach</h3>
      <div className="relative w-[280px] h-[280px] sm:w-[300px] sm:h-[300px] md:w-[400px] md:h-[400px]">
        {/* Top */}
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 w-32 h-32 sm:w-40 sm:h-40 rounded-full bg-blue-100 border-4 border-blue-300 flex items-center justify-center text-center p-2 z-10 opacity-90">
          <span className="font-bold text-blue-900 text-sm md:text-base">Administration</span>
        </div>
        {/* Left */}
        <div className="absolute top-1/2 left-0 transform -translate-y-1/2 w-32 h-32 sm:w-40 sm:h-40 rounded-full bg-green-100 border-4 border-green-300 flex items-center justify-center text-center p-2 z-10 opacity-90">
          <span className="font-bold text-green-900 text-sm md:text-base">Evaluation</span>
        </div>
        {/* Right */}
        <div className="absolute top-1/2 right-0 transform -translate-y-1/2 w-32 h-32 sm:w-40 sm:h-40 rounded-full bg-purple-100 border-4 border-purple-300 flex items-center justify-center text-center p-2 z-10 opacity-90">
          <span className="font-bold text-purple-900 text-sm md:text-base">Training</span>
        </div>
        {/* Bottom */}
        <div className="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-32 h-32 sm:w-40 sm:h-40 rounded-full bg-orange-100 border-4 border-orange-300 flex items-center justify-center text-center p-2 z-10 opacity-90">
          <span className="font-bold text-orange-900 text-sm md:text-base">Consultation</span>
        </div>
        
        {/* Center Intersection */}
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-16 h-16 rounded-full bg-slate-800 text-white flex items-center justify-center z-20 shadow-lg">
          <span className="text-xs font-bold">PEM</span>
        </div>
      </div>
      <div className="mt-12 text-sm text-slate-500 text-center max-w-lg px-4">
        The PEM Foundations Workshop is the first piece (Training). The system relies on the interplay of all four components.
      </div>
    </div>
  );
}

function BPSDiagram() {
  return (
    <div className="flex flex-col items-center overflow-x-auto">
      <div className="min-w-[600px] flex flex-col items-center">
        <div className="bg-slate-800 text-white px-6 py-3 rounded-lg font-bold mb-4 shadow-md">Psychoeducational Model</div>
        <div className="w-0.5 h-8 bg-slate-300"></div>
        <div className="flex gap-4 md:gap-12 relative">
          <div className="absolute top-0 left-10 right-10 h-0.5 bg-slate-300"></div>
          {/* Branch 1 */}
          <div className="flex flex-col items-center pt-4">
            <div className="w-0.5 h-4 bg-slate-300 absolute -top-0"></div>
            <div className="bg-white border-2 border-slate-300 px-4 py-2 rounded font-semibold mb-4 w-32 text-center">Biological</div>
            <div className="w-0.5 h-4 bg-slate-300"></div>
            <div className="bg-slate-100 px-3 py-1 rounded text-sm w-32 text-center border border-slate-200">Medical</div>
          </div>
          {/* Branch 2 */}
          <div className="flex flex-col items-center pt-4">
            <div className="w-0.5 h-4 bg-slate-300 absolute -top-0"></div>
            <div className="bg-white border-2 border-slate-300 px-4 py-2 rounded font-semibold mb-4 w-32 text-center">Psychological</div>
            <div className="flex flex-col gap-2">
              <div className="bg-slate-100 px-3 py-1 rounded text-sm w-32 text-center border border-slate-200">Family Therapy</div>
              <div className="bg-slate-100 px-3 py-1 rounded text-sm w-32 text-center border border-slate-200">Individual Therapy</div>
              <div className="bg-slate-100 px-3 py-1 rounded text-sm w-32 text-center border border-slate-200">Group Therapy</div>
            </div>
          </div>
          {/* Branch 3 */}
          <div className="flex flex-col items-center pt-4">
            <div className="w-0.5 h-4 bg-slate-300 absolute -top-0"></div>
            <div className="bg-white border-2 border-slate-300 px-4 py-2 rounded font-semibold mb-4 w-32 text-center">Social</div>
            <div className="flex flex-col gap-2">
              <div className="bg-slate-100 px-3 py-1 rounded text-sm w-32 text-center border border-slate-200">Social Skills</div>
              <div className="bg-slate-100 px-3 py-1 rounded text-sm w-32 text-center border border-slate-200">Modeling</div>
              <div className="bg-slate-100 px-3 py-1 rounded text-sm w-32 text-center border border-slate-200">Teaching Interactions</div>
            </div>
          </div>
        </div>
      </div>
      <div className="text-xs text-slate-400 mt-2 md:hidden">Scroll right to see full diagram &rarr;</div>
    </div>
  );
}

function ProfessionalismContent() {
  return (
    <div className="space-y-6">
      <p className="text-slate-700">
        Professionals are viewed as experts who are competent, caring, and cooperative. Being a professional means living by a code of behavior and ethics.
      </p>
      <div className="bg-slate-100 p-6 rounded-xl">
        <h4 className="font-bold text-slate-800 mb-4 flex items-center"><Award size={18} className="mr-2" /> Code of Behavior & Ethics</h4>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-3">
          {[
            "Implementing the PEM Model",
            "Modeling appropriate behavior",
            "Respecting Cultural Diversity",
            "Fostering Positive Consumer Relationships",
            "Continuing to develop skills",
            "Maintaining Professional Boundaries"
          ].map((item, i) => (
             <div key={i} className="flex items-center text-sm text-slate-700">
               <div className="w-2 h-2 rounded-full bg-slate-400 mr-2 flex-shrink-0"></div>
               {item}
             </div>
          ))}
        </div>
      </div>
      <div className="mt-6">
        <h4 className="font-bold text-slate-800 mb-2">Respecting Cultural Diversity</h4>
        <p className="text-sm text-slate-600">
          Valuing differences helps build better relationships. For example, eye contact norms vary by culture. While PEM teaches "Look at the person," staff must be sensitive to cultural origins of behavior to avoid taking things personally.
        </p>
      </div>
    </div>
  );
}

function ProfessionalGrowthContent() {
  return (
    <div className="space-y-8">
      {/* Feedback Section */}
      <div className="space-y-4">
        <div className="flex items-center">
          <MessageCircle className="text-blue-600 mr-2" />
          <h3 className="text-xl font-bold text-slate-800">Constructive Feedback</h3>
        </div>
        <p className="text-slate-600 text-sm">Feedback is information about the effects of one's behavior. It is essential for learning and professional growth.</p>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-green-50 p-4 rounded-lg border border-green-100">
            <h4 className="font-bold text-green-900 text-sm mb-2">Providing Feedback</h4>
            <ul className="text-xs text-green-800 space-y-1 list-disc list-inside">
              <li>Convey positive intent</li>
              <li>Describe specific observations</li>
              <li>State the impact</li>
              <li>Focus on solutions</li>
            </ul>
          </div>
          <div className="bg-blue-50 p-4 rounded-lg border border-blue-100">
            <h4 className="font-bold text-blue-900 text-sm mb-2">Accepting Feedback</h4>
            <ul className="text-xs text-blue-800 space-y-1 list-disc list-inside">
              <li>Focus on content, not person</li>
              <li>Listen calmly</li>
              <li>Avoid defending</li>
              <li>Welcome suggestions</li>
            </ul>
          </div>
        </div>
      </div>

      <hr className="border-slate-200" />

      {/* Communication & Confidentiality */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h4 className="font-bold text-slate-800 mb-2">Communication</h4>
          <p className="text-sm text-slate-600 mb-2">
            Clear, frequent, and pleasant communication is a hallmark of professionalism.
          </p>
          <div className="bg-white p-3 border rounded shadow-sm text-xs text-slate-600">
            <strong>Solution-Focused Morale Boosting:</strong> Focus on situations, maintain self-esteem, and take initiative to make things better.
          </div>
        </div>
        
        <div>
          <div className="flex items-center mb-2">
            <Lock size={16} className="text-slate-500 mr-2" />
            <h4 className="font-bold text-slate-800">Confidentiality</h4>
          </div>
          <p className="text-sm text-slate-600">
            You must be sure that confidential information is shared only with persons who have a legitimate need for it. This preserves integrity and trust.
          </p>
        </div>
      </div>
    </div>
  );
}

function BoundariesContent() {
  return (
    <div className="space-y-6">
      <div className="flex items-start bg-red-50 p-4 rounded-lg border border-red-100">
        <AlertCircle className="text-red-500 mt-1 mr-3 flex-shrink-0" />
        <div>
          <h4 className="font-bold text-red-800">Boundary Violations</h4>
          <p className="text-sm text-red-700 mt-1">
            80% of youth in placement report having been sexually abused and may have damaged perceptions of healthy boundaries.
          </p>
        </div>
      </div>

      <div className="space-y-4">
        <h4 className="font-bold text-slate-800">Types of Boundaries to Watch</h4>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
           {[
             { title: "Role", desc: "Doing things not part of your job." },
             { title: "Time", desc: "Spending more time with one youth than others." },
             { title: "Money", desc: "Giving money or gifts." },
             { title: "Clothing", desc: "Dressing seductively or unprofessionally." },
             { title: "Self-Disclosure", desc: "Sharing personal info without therapeutic value." },
             { title: "Physical Contact", desc: "Touching in unnecessary/suggestive ways." },
           ].map((b, i) => (
             <div key={i} className="bg-white border p-3 rounded shadow-sm">
               <strong className="block text-slate-800">{b.title}</strong>
               <span className="text-xs text-slate-500">{b.desc}</span>
             </div>
           ))}
        </div>
      </div>
    </div>
  );
}

function RelationshipsContent() {
  return (
    <div className="space-y-6">
       <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
         <div className="bg-slate-50 p-4 rounded-lg">
           <div className="font-bold text-blue-600 mb-1">1. Goal Oriented</div>
           <p className="text-xs text-slate-600">Relationship exists to help youth meet specific goals.</p>
         </div>
         <div className="bg-slate-50 p-4 rounded-lg">
           <div className="font-bold text-blue-600 mb-1">2. Time Limited</div>
           <p className="text-xs text-slate-600">Ends when goals are met or treatment concludes.</p>
         </div>
         <div className="bg-slate-50 p-4 rounded-lg">
           <div className="font-bold text-blue-600 mb-1">3. Power Differential</div>
           <p className="text-xs text-slate-600">Staff have authority/resources youth do not.</p>
         </div>
         <div className="bg-slate-50 p-4 rounded-lg">
           <div className="font-bold text-blue-600 mb-1">4. Non-Reciprocal</div>
           <p className="text-xs text-slate-600">Staff meet youth needs; youth do NOT meet staff needs.</p>
         </div>
       </div>
    </div>
  );
}

function QualityComponentsDiagram() {
  return (
    <div className="flex flex-col items-center justify-center space-y-8">
       <h3 className="text-xl font-bold text-center">Quality Components</h3>
       <div className="flex flex-col md:flex-row items-center justify-center gap-8 flex-wrap">
          <div className="relative w-48 h-48 md:w-64 md:h-64 flex-shrink-0">
             <svg viewBox="0 0 100 100" className="w-full h-full transform -rotate-90">
               <circle r="25" cx="50" cy="50" fill="transparent" stroke="#3b82f6" strokeWidth="50" strokeDasharray="58 100" />
               <circle r="25" cx="50" cy="50" fill="transparent" stroke="#7dd3fc" strokeWidth="50" strokeDasharray="35 100" strokeDashoffset="-58" />
               <circle r="25" cx="50" cy="50" fill="transparent" stroke="#1e293b" strokeWidth="50" strokeDasharray="7 100" strokeDashoffset="-93" />
             </svg>
             <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
                <span className="text-xs font-bold text-white z-10">93% Non-Verbal</span>
             </div>
          </div>
          <div className="space-y-2 text-sm">
             <div className="flex items-center"><div className="w-3 h-3 bg-blue-500 mr-2 rounded"></div> Body Language (58%)</div>
             <div className="flex items-center"><div className="w-3 h-3 bg-sky-300 mr-2 rounded"></div> Voice Tone (35%)</div>
             <div className="flex items-center"><div className="w-3 h-3 bg-slate-800 mr-2 rounded"></div> Word Choice (7%)</div>
          </div>
       </div>
    </div>
  );
}

function WillnerSortGame() {
  const [items, setItems] = useState([...WILLNER_LIKED, ...WILLNER_DISLIKED].sort(() => Math.random() - 0.5));
  const [currentItem, setCurrentItem] = useState(0);
  const [feedback, setFeedback] = useState<string | null>(null);

  const handleChoice = (type: 'liked' | 'disliked') => {
    const item = items[currentItem];
    const isLiked = WILLNER_LIKED.includes(item);
    const isCorrect = (type === 'liked' && isLiked) || (type === 'disliked' && !isLiked);
    setFeedback(isCorrect ? "Correct!" : "Incorrect.");
    setTimeout(() => {
      setFeedback(null);
      if (currentItem < items.length - 1) setCurrentItem(currentItem + 1);
    }, 800);
  };

  if (currentItem >= items.length) return <div className="text-center py-12 font-bold">Activity Complete!</div>;

  return (
    <div className="max-w-md mx-auto text-center py-8">
      <h3 className="text-lg font-bold mb-2">Willner Study Activity</h3>
      <div className="h-32 flex items-center justify-center bg-white border-2 border-slate-200 rounded-xl shadow-sm mb-8 px-6">
        <span className="text-xl font-medium text-slate-800">{items[currentItem]}</span>
      </div>
      {feedback && <div className={`mb-4 font-bold ${feedback === "Correct!" ? "text-green-600" : "text-red-500"}`}>{feedback}</div>}
      <div className="grid grid-cols-2 gap-4">
        <button onClick={() => handleChoice('liked')} className="bg-green-100 text-green-800 py-4 rounded-xl font-bold flex flex-col items-center"><CheckCircle className="mb-2" /> Youth LIKE</button>
        <button onClick={() => handleChoice('disliked')} className="bg-red-100 text-red-800 py-4 rounded-xl font-bold flex flex-col items-center"><X className="mb-2" /> Youth DISLIKE</button>
      </div>
    </div>
  );
}

function BehaviorSortGame() {
  const [idx, setIdx] = useState(0);
  const [feedback, setFeedback] = useState<string | null>(null);

  const handleChoice = (choice: string) => {
    const item = BEHAVIOR_VS_LABEL[idx];
    if (choice === item.category) {
       setFeedback(item.feedback);
       setTimeout(() => { setFeedback(null); if (idx < BEHAVIOR_VS_LABEL.length - 1) setIdx(idx + 1); }, 1500);
    } else {
       setFeedback("Incorrect. Try again!");
    }
  };

  if (idx >= BEHAVIOR_VS_LABEL.length) return <div className="text-center py-12 font-bold">Activity Complete!</div>;

  return (
    <div className="max-w-md mx-auto text-center py-8">
      <h3 className="text-lg font-bold mb-4">Behavior vs. Label</h3>
      <div className="bg-white border-2 border-slate-200 rounded-xl p-8 mb-6 shadow-sm min-h-[120px] flex items-center justify-center">
         <span className="text-xl font-medium text-slate-800">{BEHAVIOR_VS_LABEL[idx].text}</span>
      </div>
      {feedback && <div className="mb-4 text-blue-600 font-bold">{feedback}</div>}
      <div className="grid grid-cols-2 gap-4">
        <button onClick={() => handleChoice('behavior')} className="bg-indigo-100 text-indigo-900 py-3 rounded-lg font-bold">Specific Behavior</button>
        <button onClick={() => handleChoice('label')} className="bg-orange-100 text-orange-900 py-3 rounded-lg font-bold">Label / Judgment</button>
      </div>
    </div>
  );
}

function RationaleQuiz() {
  const [idx, setIdx] = useState(0);
  const [feedback, setFeedback] = useState<string | null>(null);

  const handleChoice = (i: number) => {
    const scenario = RATIONALE_SCENARIOS[idx];
    if (i === scenario.correctIndex) {
      setFeedback(`Correct! ${scenario.explanation}`);
      setTimeout(() => { setFeedback(null); if (idx < RATIONALE_SCENARIOS.length - 1) setIdx(idx + 1); }, 2500);
    } else {
      setFeedback("Incorrect. Try the other option.");
    }
  };

  if (idx >= RATIONALE_SCENARIOS.length) return <div className="text-center py-12 font-bold">Activity Complete!</div>;

  const scenario = RATIONALE_SCENARIOS[idx];

  return (
    <div className="max-w-xl mx-auto py-8">
      <h3 className="text-lg font-bold mb-2">Select the Effective Rationale</h3>
      <p className="text-sm text-slate-500 mb-6">Scenario: <strong>{scenario.situation}</strong></p>
      <div className="space-y-4">
        {scenario.options.map((opt, i) => (
          <button key={i} onClick={() => handleChoice(i)} className="w-full text-left p-4 bg-white border border-slate-200 rounded-lg hover:bg-blue-50 transition-all text-sm">{opt}</button>
        ))}
      </div>
      {feedback && <div className="mt-6 p-4 bg-green-50 text-green-800 rounded border border-green-200 font-medium">{feedback}</div>}
    </div>
  );
}

function QuizComponent({ data, scores, setScores }: { id: string, data: QuizQuestion[], scores: any, setScores: any }) {
  const [currentQ, setCurrentQ] = useState(0);
  const [showResult, setShowResult] = useState(false);

  const handleAnswer = (idx: number) => {
    setShowResult(true);
  };

  const nextQ = () => {
    setShowResult(false);
    if (currentQ < data.length - 1) setCurrentQ(currentQ + 1);
  };

  const question = data[currentQ];

  return (
    <div className="max-w-xl mx-auto py-8">
      <div className="flex items-center justify-between mb-6">
         <h3 className="font-bold text-slate-800">Question {currentQ + 1}/{data.length}</h3>
      </div>
      <div className="mb-6 text-lg font-medium text-slate-900">{question.question}</div>
      <div className="space-y-3">
        {question.options.map((opt, idx) => (
          <button
            key={idx}
            onClick={() => !showResult && handleAnswer(idx)}
            className={`w-full text-left p-4 rounded-lg border transition-all ${showResult ? idx === question.correctIndex ? 'bg-green-100 border-green-300 text-green-900' : 'bg-white' : 'bg-white hover:bg-blue-50'}`}
          >
            {opt}
          </button>
        ))}
      </div>
      {showResult && currentQ < data.length - 1 && <button onClick={nextQ} className="mt-6 text-blue-600 font-bold hover:underline flex items-center">Next Question <ChevronRight size={16} /></button>}
    </div>
  );
}

function Card({ title, children, icon }: { title: string, children: React.ReactNode, icon: React.ReactNode }) {
  return (
    <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
      <div className="flex items-center mb-3">
        {icon}
        <h4 className="ml-2 font-bold text-slate-800">{title}</h4>
      </div>
      <p className="text-sm text-slate-600 leading-relaxed">{children}</p>
    </div>
  );
}

function JournalActivity({ id, prompt, entries, setEntries }: { id: string, prompt: string, entries: Record<string, string>, setEntries: any }) {
  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setEntries({ ...entries, [id]: e.target.value });
  };

  return (
    <div className="bg-yellow-50 p-6 rounded-xl border border-yellow-200 shadow-sm">
      <div className="flex items-center mb-4 text-yellow-800">
        <Edit3 size={20} className="mr-2" />
        <h3 className="font-bold">Reflection Activity</h3>
      </div>
      <p className="mb-4 text-slate-700 font-medium">{prompt}</p>
      <textarea
        className="w-full h-32 p-4 rounded-lg border border-yellow-300 focus:ring-2 focus:ring-yellow-400 focus:outline-none text-slate-700 bg-white"
        placeholder="Type your thoughts here..."
        value={entries[id] || ''}
        onChange={handleChange}
      />
      <p className="mt-2 text-xs text-slate-500 italic">Your responses are saved while this tab is open.</p>
    </div>
  );
}
