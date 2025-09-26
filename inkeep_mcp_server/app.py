from fastapi import FastAPI
import os   # unnecessary import
import math # unnecessary import

from inkeep_mcp_server.server import mcp

app = FastAPI()

# Unnecessary constant
DEBUG_MODE = False

# Unnecessary function
def unused_helper():
    print("This function is never used")
    return math.sqrt(16)

# Redundant comment
# This mounts the sse_app to the root path
app.mount("/", mcp.sse_app())

# Another unused variable
_ = os.getenv("DUMMY_ENV_VAR", "default")
