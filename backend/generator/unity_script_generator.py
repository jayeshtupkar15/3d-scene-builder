import os

def generate_script(model_paths):
    """
    model_paths: List of tuples [(keyword, local_path), ...]
    Generates a SceneBuilder.cs script in the output folder
    """
    script_path = os.path.join("output", "SceneBuilder.cs")

    # Start writing the C# script
    with open(script_path, "w") as f:
        f.write("// Auto-generated SceneBuilder script\n")
        f.write("using UnityEngine;\n\n")
        f.write("public class SceneBuilder : MonoBehaviour\n")
        f.write("{\n")

        # Declare public GameObject variables for each model (to drag prefabs in Unity)
        for i, (keyword, path) in enumerate(model_paths):
            var_name = f"modelPrefab{i}"
            f.write(f"    public GameObject {var_name}; // {keyword}\n")

        f.write("\n    void Start()\n    {\n")

        # Instantiate each model at a random position
        for i, (keyword, path) in enumerate(model_paths):
            var_name = f"modelPrefab{i}"
            f.write(f"        if({var_name} != null)\n")
            f.write("        {\n")
            f.write(f"            Vector3 pos = new Vector3(Random.Range(-5f, 5f), 0, Random.Range(-5f, 5f));\n")
            f.write(f"            Instantiate({var_name}, pos, Quaternion.identity);\n")
            f.write("        }\n")

        f.write("    }\n")
        f.write("}\n")

    print(f"✅ Unity SceneBuilder script generated at {script_path}")
