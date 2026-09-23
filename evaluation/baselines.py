"""B1-B5 reproducible controller/retrieval ablations.
B1 final-only BM25; B2 every-chunk BM25; B3 final hybrid; B4 streaming hybrid no decomposition;
B5 full Streaming Live RAG. Use these labels in comparative reports.
"""
BASELINES={'B1':'final_only_bm25','B2':'every_chunk_bm25','B3':'final_hybrid','B4':'streaming_no_decomposition','B5':'streaming_live_rag'}
ABLATIONS={'A1_no_wait_controller':'retrieve each chunk','A2_no_delta_refinement':'full rerun after late constraint'}
