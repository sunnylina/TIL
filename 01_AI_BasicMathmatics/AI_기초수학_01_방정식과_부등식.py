{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "AI 기초수학_01 방정식과 부등식.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LNU4uunYsDpA",
        "outputId": "afeb4e84-fff5-4873-f4b9-2254f5572102"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        }
      ],
      "source": [
        "# 변수 \n",
        "\n",
        "x = 5\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x,y,z=1,2,3\n",
        "print(x,y,z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SMIxe5iLskWt",
        "outputId": "305ea3b9-e6d1-46ca-d609-114b06f99924"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 방정식 \n",
        "\n",
        "# sympy() \n",
        "from sympy import Symbol, solve\n",
        "x = Symbol('x')\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 38
        },
        "id": "ITRu2p2JsqFY",
        "outputId": "111d250a-19c1-45e7-8337-7f3fc276ad0c"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "x"
            ],
            "text/latex": "$\\displaystyle x$"
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "equation = 2 * x - 6\n",
        "solve(equation)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dr1wgcnJsqIS",
        "outputId": "c08d7303-5277-45ad-a39b-a62cccd8b4b1"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[3]"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 4 = k-2 >> k - 2 - 4 = 0\n",
        "# k= 4+2 =6\n",
        "\n",
        "k = Symbol('k')\n",
        "equation = k - 2 - 4\n",
        "solve(equation)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BtYjV_w4sqKn",
        "outputId": "80fab6a5-7c7c-4f96-ce98-93595ee2a513"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[6]"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 10 = 2k \n",
        "# k = 10/2 = 5\n",
        "\n",
        "k = Symbol('k')\n",
        "equation = 2 * k - 10\n",
        "solve(equation)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qD_jR1JIusGm",
        "outputId": "3f05d5fc-1b99-4b31-edb6-ef872b8f009c"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[5]"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# k / 2 = 8\n",
        "# k = 2 * 8 = 16\n",
        "\n",
        "k = Symbol('k')\n",
        "equation = k / 2 - 8\n",
        "solve(equation)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OtTABCaduui5",
        "outputId": "8fe221f6-f82d-49d3-d45f-5daa9aef8ac2"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[16]"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 연립방정식 \n",
        "\n",
        "x = Symbol('x')\n",
        "y = Symbol('y')"
      ],
      "metadata": {
        "id": "uySLh0M-uulR"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 일차방정식 = 0 형태로 만들어 주세요\n",
        "equ1 = 3*x+y-2\n",
        "equ2 = x-2*y-3"
      ],
      "metadata": {
        "id": "NybBLAbjvo5x"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "solve((equ1, equ2))  # dict() 형태 "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QGglLMzUvo8R",
        "outputId": "b7743cbb-a057-4c46-f42e-7002312f12ef"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{x: 1, y: -1}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "solve((equ1, equ2),dict=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4WaiPaVGvo-w",
        "outputId": "6c851eb4-ca23-4767-d61a-7444468422ed"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{x: 1, y: -1}]"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "DguLnj29uuno"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "e75o06tWuup4"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}