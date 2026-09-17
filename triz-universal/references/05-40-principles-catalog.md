---
description: >-
  Concise, high-density catalog of all 40 Altshuller Inventive Principles mapped across software, AI, business, and physical engineering.
metadata:
  tags: [40-principles, inventive-principles, catalog, multi-domain, software, business]
  source: TRIZ-Classical & Modern
---

# 05. The 40 Inventive Principles (Universal Multi-Domain Catalog)

Use this catalog when seeking inventive mechanisms to implement a Separation Operator or resolve a stubborn Technical Contradiction.

---

| # | Principle Name | Classical Meaning | Software & Systems Mapping | Business & Strategy Mapping |
|---|---|---|---|---|
| **1** | **Segmentation** | Divide an object into independent parts; make it sectional. | Microservices, database sharding, pagination, SIMD data parallelism. | Modular subscription pricing, dividing large projects into autonomous squads. |
| **2** | **Taking Out / Extraction** | Extract only the necessary part or property; separate disturbing parts. | Separation of Concerns (SoC); offload CPU tasks to worker threads; GraphQL sparse fields. | Outsourcing non-core commoditized operations; unbundling complex product suites. |
| **3** | **Local Quality** | Transition from uniform to non-uniform structure; give each part specialized function. | Hot/cold memory tiering; indexing only active rows (partial indexes); inner loops in Rust. | VIP customer onboarding tracks; tier-based service level agreements (SLAs). |
| **4** | **Asymmetry** | Replace symmetrical form with asymmetrical. | CQRS (asymmetric read vs write data models); public/private keys; read replicas. | Freemium monetization asymmetry (free for consumers, paid for merchants). |
| **5** | **Merging / Consolidation** | Combine identical or related objects; perform parallel operations. | Bulk database operations; HTTP/2 stream multiplexing; connection pooling. | Mergers & acquisitions; co-marketing partnerships; bundling complementary services. |
| **6** | **Universality** | Make an object perform multiple functions, eliminating other parts. | Generic programming (generics, templates); multi-purpose protocols (gRPC). | Full-stack cross-functional teams; multi-purpose mobile super-apps (WeChat). |
| **7** | **"Nested Doll" (Matryoshka)** | Place one object inside another, which is placed inside another. | Middleware chains; layered network protocols (OSI stack); containers in VMs. | Subsidiarity in corporate hierarchy; nested product ecosystems (Apple ecosystem). |
| **8** | **Anti-Weight / Counterweight** | Compensate for weight by combining with lifting force. | Reactive Streams backpressure; circuit breakers shedding load; GC reference balancing. | Hedging financial downside with inverse derivatives; escrow milestone releases. |
| **9** | **Preliminary Anti-Action** | If action causes harmful effects, apply opposing action beforehand. | Defensive input sanitization; Zod schema validation; token bucket rate limiting. | Non-disclosure agreements (NDAs) before pitches; pre-mortems before project launch. |
| **10** | **Preliminary Action** | Perform required action (fully or partially) in advance. | Static Site Generation (SSG); pre-fetching; JIT warm-up; materialized views. | Pre-ordering and Kickstarter campaigns to validate demand before manufacturing. |
| **11** | **Cushion in Advance** | Compensate for low reliability by preparing emergency countermeasures. | Retry with exponential backoff and jitter; dead-letter queues (DLQ); fallback cache. | Emergency credit lines; contingency disaster recovery protocols; indemnity clauses. |
| **12** | **Equipotentiality** | Avoid lifting or lowering objects in potential field. | Zero-copy kernel buffers (`sendfile`); stateless web tiers behind round-robin balancers. | Flat organizational hierarchy; lateral internal career mobility without salary cliffs. |
| **13** | **The Other Way Around** | Invert the action; make moving parts fixed and fixed parts moving. | Inversion of Control (IoC); Dependency Injection; Reactive pull streams; TDD. | Reverse auctions (buyers set price, suppliers bid); user-generated content models. |
| **14** | **Spheroidality / Curvature** | Replace flat surfaces with curved; linear motion with rotary. | Ring buffers (LMAX Disruptor) for lock-free IPC; circular event loops; token buckets. | Continuous feedback loops instead of annual reviews; cyclical product release trains. |
| **15** | **Dynamics** | Make an object or process adapt dynamically to changing conditions. | Feature flags; dynamic config reload without restart; autoscaling compute pods. | Surge pricing (Uber); agile sprint reallocation based on live customer metrics. |
| **16** | **Partial or Excessive Action** | If 100% is hard, do slightly less or slightly more to simplify. | Optimistic UI updates; Bloom filters (probabilistic set testing); branch prediction. | Minimal Viable Product (MVP) testing; over-subscribing initial waitlist invites. |
| **17** | **Another Dimension** | Move from 1D to 2D/3D; use multi-story or spatial arrangements. | Switching row-oriented to columnar storage (ClickHouse/DuckDB); GPU vectorization. | Pivoting from 1D transactional sales to 2D platform marketplace ecosystem. |
| **18** | **Mechanical Vibration** | Cause an object to oscillate or vibrate. | Random jitter in network retries; node heartbeats; replacing polling with events. | Pulse surveys to measure employee morale; periodic flash promotions. |
| **19** | **Periodic Action** | Replace continuous action with periodic or pulsed action. | Scheduled cron jobs; micro-batching flushes every 10ms; controller reconciliation. | Bi-weekly sprint retrospectives; quarterly board reviews; seasonal marketing drops. |
| **20** | **Continuity of Useful Action** | Keep all parts working at full capacity without idle intervals. | Streaming data pipelines; non-blocking async I/O (`epoll`, `io_uring`); pipelining. | 24/7 global follow-the-sun customer support across distributed timezones. |
| **21** | **Skipping / Hurrying Through** | Conduct process at high speed to pass through dangerous stages. | Short-circuit boolean evaluation; fail-fast validation; speculative fast-path bypass. | Blitzscaling to achieve network effects before competitors can react. |
| **22** | **Blessing in Disguise** | Use harmful factors to achieve positive effect. | Chaos engineering (breaking nodes to expose bugs); traffic spikes warming caches. | Turning a public PR crisis into a transparency showcase that builds customer trust. |
| **23** | **Feedback** | Introduce feedback to improve process or action. | Closed-loop PID autoscalers; TCP congestion control (BBR); adaptive query planning. | Net Promoter Score (NPS) telemetry driving product roadmap prioritizations. |
| **24** | **Intermediary** | Use intermediate carrier or process to transfer action. | Reverse proxies (Envoy/Nginx); message brokers (Kafka); Adapter/Facade patterns. | Merchant of Record (Stripe/Paddle) handling global VAT compliance for SaaS. |
| **25** | **Self-Service** | Make object service itself by performing auxiliary operations. | Kubernetes self-healing restarts; autonomous index defragmentation; OpenAPI. | Customer self-serve knowledge base; automated password reset flows. |
| **26** | **Copying** | Use simple/cheap copy instead of fragile or expensive original. | Read replicas; CDN edge caching; database snapshots; digital twin test environments. | Staging environments mirroring production; simulation war-games for executive strategy. |
| **27** | **Cheap Short-Living Objects** | Replace expensive durable object with multiple cheap, ephemeral ones. | Ephemeral serverless functions (AWS Lambda); immutable data structures. | Disposable pop-up stores; temporary contractor teams for exploratory spikes. |
| **28** | **Mechanics Substitution** | Replace mechanical system with optical, acoustic, or electrical. | Replacing busy polling with WebSockets; replacing context switches with eBPF. | Replacing physical paper signatures with cryptographic electronic signatures (DocuSign). |
| **29** | **Pneumatics & Hydraulics** | Use gas or liquid parts instead of solid parts. | Elastic reactive stream buffers; fluid traffic shaping with leaky bucket algorithms. | Elastic compensation budgets that adjust fluidly to team performance. |
| **30** | **Flexible Shells & Thin Films** | Use flexible shells and thin films instead of three-dimensional structures. | Lightweight WebAssembly (Wasm) sandboxes; thin API facades; micro-frontends. | Lightweight landing page funnels testing demand before developing the core product. |
| **31** | **Porous Materials** | Make an object porous or introduce porous elements. | Sparse matrices and sparse files; bitmasks (Roaring Bitmaps); sparse indexes. | Open-door policy allowing informal cross-department communication channels. |
| **32** | **Color Changes** | Change color or transparency; use color additives. | State tagging; Blue-Green / Canary deployment traffic tagging; color-coded log levels. | Transparent salary bands; public roadmaps demonstrating product trust. |
| **33** | **Homogeneity** | Make objects interacting with primary object from identical material. | Monorepos enforcing uniform standards; Protobuf serialization; uniform Linux images. | Standardized corporate OKRs and shared company cultural values across all offices. |
| **34** | **Discarding & Recovering** | Discard portions that fulfilled function; restore consumable parts. | Generational Garbage Collection; cycling unhealthy pods; session token refresh. | Sunset obsolete legacy product tiers; rotating quarterly executive assignments. |
| **35** | **Parameter Changes** | Change physical state, concentration, density, or temperature. | Transpilation; payload compression (Zstandard); switching JSON to binary format. | Shifting pricing from upfront perpetual license to recurring monthly SaaS subscription. |
| **36** | **Phase Transitions** | Utilize phenomena occurring during phase transitions. | JIT compilation (bytecode $\to$ native); object freezing (mutable $\to$ immutable). | Transitioning a viral product from invite-only private beta to public general availability. |
| **37** | **Thermal Expansion** | Use expansion or contraction of materials. | Elastic autoscaling expanding under CPU load; dynamic array geometric resizing. | Elastic hiring surges during seasonal retail demand followed by post-holiday normalization. |
| **38** | **Strong Oxidants** | Accelerate oxidation; use enriched or active environments. | Aggressive compiler inlining & Dead Code Elimination; Chaos Monkey; `-Werror`. | High-intensity incubator hackathons forcing rapid 48-hour prototype delivery. |
| **39** | **Inert Atmosphere** | Replace normal environment with inert medium to prevent degradation. | Read-only container root filesystems; isolated microVM sandboxes (Firecracker). | Regulatory sandbox environments allowing fintech experimentation without license exposure. |
| **40** | **Composite Materials** | Replace uniform material with composite (multi-layered) structure. | Polyglot persistence (SQL + Cache + Search); hybrid Python + Rust FFI extensions. | Hybrid business models combining automated software margins with premium human advisory. |

---

**Next:** [06-system-operator-9screens.md](06-system-operator-9screens.md) — System Operator (9 Screens) & Anti-System.  
**Index:** [README.md](README.md)
