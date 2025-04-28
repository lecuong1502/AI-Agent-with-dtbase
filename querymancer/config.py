import os 
import random
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

class ModelProvider(str, Enum):
    OLLAMA = "ollama"
    GROQ = "groq"
    
@dataclass
class ModelConfig:
    name: str
    temperature: float #Control the random output (type: float)
    provider: ModelProvider
    
QWEN_2_5 = ModelConfig("qwen2.5", 0.0, ModelProvider.OLLAMA)
GEMMMA_3 = ModelConfig(
    "PetrosStav/gemma3-tools:12b", 0.7, ModelProvider.OLLAMA
) # doesn't work that well
LLAMA_3_3 = ModelConfig("llama-3.3-70b-versatile", 0.0, ModelProvider.GROQ)

class Config:
    SEED = 42
    MODEL = QWEN_2_5
    OLLAMA_CONTEXT_WINDOW = 2848 #increase to allow longer conversation but slower response 
    
    class Path:
        APP_HOME = Path(os.getenv("APP_HOME", Path(__file__).parent.parent))
        DATA_DIR = APP_HOME / "data"
        DATABASE_PATH = DATA_DIR / "ecomerce.sqlite"
        
def seed_everything(seed: int = Config.SEED):
    random.seed(seed)